#!/usr/bin/env python3

import argparse
import logging

import arc852.cli_args as cli
from arc852.constants import SERIAL_PORT, BAUD_RATE, MQTT_HOST, LOG_LEVEL, TOPIC, DEVICE_ID, OOR_SIZE, OOR_TIME
from arc852.moving_average import MovingAverage
from arc852.mqtt_connection import MqttConnection, PAHO_CLIENT
from arc852.out_of_range_values import OutOfRangeValues
from arc852.serial_reader import SerialReader
from arc852.utils import setup_logging, waitForKeyboardInterrupt

import frc_utils
from frc_utils import COMMAND, ENABLED, MOVING_AVERAGE, DEVICE, AVG_SIZE
from short_lidar_publisher import OOR_VALUES

logger = logging.getLogger(__name__)

TOLERANCE_THRESH = 2.5


def on_connect(mqtt_client, userdata, flags, rc):
    logger.info("Connected with result code: %s", rc)
    mqtt_client.subscribe(userdata[COMMAND])


def fetch_data(cm_str, userdata):
    topic = userdata[TOPIC]
    client = userdata[PAHO_CLIENT]
    moving_avg = userdata[MOVING_AVERAGE]
    oor_values = userdata[OOR_VALUES]

    cm = int(cm_str)

    if cm <= 0:
        return

    moving_avg.add(cm)
    avg = moving_avg.average()

    if not userdata[ENABLED]:
        return

    # if abs(cm - avg) > TOLERANCE_THRESH:
    #    client.publish(topic, payload=str(cm).encode("utf-8"), qos=0)

    if len(moving_avg) == moving_avg.max_size():
        client.publish(topic, payload=str(int(avg)).encode("utf-8"), qos=0)
        moving_avg.clear()


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.device_id(parser)
    cli.serial_port(parser)
    cli.baud_rate(parser)
    cli.oor_size(parser)
    cli.oor_time(parser)
    parser.add_argument("-d", "--device", dest=DEVICE, required=True, help="Device ('front' or 'rear'")
    parser.add_argument("--avg_size", dest=AVG_SIZE, default=10, type=int, help="Moving average size [10]")
    cli.log_level(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    userdata = {TOPIC: "lidar/{0}/cm".format(args[DEVICE]),
                COMMAND: "lidar/{0}/command".format(args[DEVICE]),
                ENABLED: True,
                MOVING_AVERAGE: MovingAverage(args[AVG_SIZE]),
                OOR_VALUES: OutOfRangeValues(size=args[OOR_SIZE]),
                OOR_TIME: args[OOR_TIME]}

    with SerialReader(func=fetch_data,
                      userdata=userdata,
                      port=SerialReader.lookup_port(args[DEVICE_ID]) if args.get(DEVICE_ID) else args[SERIAL_PORT],
                      baudrate=args[BAUD_RATE]):
        with MqttConnection(hostname=args[MQTT_HOST],
                            userdata=userdata,
                            on_connect=on_connect,
                            on_message=frc_utils.on_message):
            waitForKeyboardInterrupt()

    logger.info("Exiting...")
