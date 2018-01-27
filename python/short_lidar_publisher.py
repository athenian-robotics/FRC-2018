#!/usr/bin/env python3

import argparse
import logging

import cli_args as cli
from constants import *
from moving_average import MovingAverage
from mqtt_connection import MqttConnection, PAHO_CLIENT
from out_of_range_values import OutOfRangeValues
from serial_reader import SerialReader
from utils import setup_logging, waitForKeyboardInterrupt

import frc_utils
from frc_utils import *

import rospy
from std_msgs.msg import Int32

TOLERANCE_THRESH = 5
USE_AVG = False

logger = logging.getLogger(__name__)


def on_connect(mqtt_client, userdata, flags, rc):
    logger.info("Connected with result code: %s", rc)
    mqtt_client.subscribe(userdata[COMMAND])


def fetch_data(mm_str, userdata):
    publisher = userdata[ROS_PUBLISHER]
    moving_avg = userdata[MOVING_AVERAGE]
    oor_values = userdata[OOR_VALUES]
    oor_upper = userdata[OOR_UPPER]
    rate = userdata[ROS_RATE]

    if not userdata[frc_utils.ENABLED]:
        return

    # Values sometimes get compacted together, take the later value if that happens since it's newer
    if "\r" in mm_str:
        mm_str = mm_str.split("\r")[1]

    mm = int(mm_str)

    if oor_upper > 0 and (mm <= 155 or mm > oor_upper):
        # Filter out bad data
        oor_values.mark()
        if oor_values.is_out_of_range(userdata[OOR_TIME]):
            oor_values.clear()
            publisher.publish(ROS_OOR)
    else:
        if USE_AVG:
            moving_avg.add(mm)
            avg = moving_avg.average()
            if not avg or abs(mm - avg) > TOLERANCE_THRESH:
                publisher.publish(mm)
        else:
            publisher.publish(mm)
            rate.sleep()


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.device_id(parser)
    cli.serial_port(parser)
    cli.baud_rate(parser)
    cli.oor_size(parser)
    cli.oor_time(parser)
    cli.oor_upper(parser)
    parser.add_argument("-d", "--device", dest=DEVICE, required=True, help="Device ('left' or 'right'")
    cli.verbose(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])
    rospy.init_node('short_lidar_publisher')
    pub = rospy.Publisher('short_lidar', Int32, queue_size=10)
    rate = rospy.Rate(2)
    userdata = {TOPIC: "lidar/{0}/mm".format(args[DEVICE]),
                COMMAND: "lidar/{0}/command".format(args[DEVICE]),
                ENABLED: True,
                MOVING_AVERAGE: MovingAverage(size=3),
                OOR_VALUES: OutOfRangeValues(size=args[OOR_SIZE]),
                OOR_TIME: args[OOR_TIME],
                OOR_UPPER: args[OOR_UPPER],
                ROS_PUBLISHER: pub,
                ROS_RATE: rate
                }

    with SerialReader(func=fetch_data,
                      userdata=userdata,
                      port=SerialReader.lookup_port(args[DEVICE_ID]) if args.get(DEVICE_ID) else args[SERIAL_PORT],
                      baudrate=args[BAUD_RATE],
                      debug=True):
        with MqttConnection(hostname=args[MQTT_HOST],
                            userdata=userdata,
                            on_connect=on_connect,
                            on_message=frc_utils.on_message):
            waitForKeyboardInterrupt()

    logger.info("Exiting...")
