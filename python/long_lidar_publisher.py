#!/usr/bin/env python3

import argparse
import logging

import arc852.cli_args as cli
from arc852.constants import *
from arc852.moving_average import MovingAverage
from arc852.serial_reader import SerialReader
from arc852.utils import setup_logging, sleep

import frc_utils
from frc_utils import *

import rospy
from std_msgs.msg import Int32, Bool, String

SHORT_LIDAR_PUB = "short_lidar_pub"
SHORT_LIDAR_RATE = "short_lidar_rate"
HEALTH_PUB = "health_pub"
HEALTH_RATE = "health_rate"

TOLERANCE_THRESH = 5
USE_AVG = False

logger = logging.getLogger(__name__)

def fetch_data(mm_str, userdata):
    if not userdata[frc_utils.ENABLED]:
        logger.info("Not enabled")
        return

    # Values sometimes get compacted together, take the later value if that happens since it's newer
    if "\r" in mm_str:
        mm_str = mm_str.split("\r")[1]

    mm = int(mm_str)

    if USE_AVG:
        userdata[MOVING_AVERAGE].add(mm)
        avg = userdata[MOVING_AVERAGE].average()

        if not avg or abs(mm - avg) > TOLERANCE_THRESH:
            publisher(mm, userdata)
            logger.info("Published {} mm".format(mm))
        else:
            logger.info("Not publishing anything, lower than tolerance threshold {}".format(TOLERANCE_THRESH))

    elif mm > 8000:
        publisher(-1, userdata)
        logger.info("Published out of range (-1) to topic {}".format(userdata[TOPIC]))
    else:
        publisher(mm, userdata)
        logger.info("Published {} mm to topic {}".format(mm, userdata[TOPIC]))


def publisher(message, userdata):
    userdata[SHORT_LIDAR_PUB].publish(message)
    userdata[SHORT_LIDAR_RATE].sleep()

# def health_check_publisher(message, userdata):
#     userdata[HEALTH_PUB].publish(message)
#     userdata[HEALTH_RATE].sleep()



if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.device_id(parser)
    cli.serial_port(parser)
    cli.baud_rate(parser)
    #cli.oor_size(parser)
    #cli.oor_time(parser)
    #cli.oor_upper(parser)
    parser.add_argument("-d", "--device", dest=DEVICE, required=True, help="Device ('left' or 'right'")
    cli.verbose(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])
    logger.info("Parsed Args")

    rospy.init_node('long_lidar_publisher')
    pub = rospy.Publisher("long_lidar/{0}/mm".format(args[DEVICE]), Int32, queue_size=10)
    rate = rospy.Rate(20)
    health_pub = rospy.Publisher("long_lidar/{0}/health".format(args[DEVICE]), Bool, queue_size=10)
    health_rate = rospy.Rate(2)

    logger.info("Setup Publishers")

    userdata = {SHORT_LIDAR_PUB: pub,
                SHORT_LIDAR_RATE: rate,
                HEALTH_PUB: health_pub,
                HEALTH_RATE: health_rate,
                COMMAND: "lidar/{0}/command".format(args[DEVICE]),
                ENABLED: True,
                MOVING_AVERAGE: MovingAverage(size=3),
                #OOR_VALUES: OutOfRangeValues(size=args[OOR_SIZE]),
                #OOR_TIME: args[OOR_TIME],
                #OOR_UPPER: args[OOR_UPPER],
                }

    logger.info("Opened serial port: " + SerialReader.lookup_port(args[DEVICE_ID]))

    with SerialReader(func=fetch_data,
                      userdata=userdata,
                      port=SerialReader.lookup_port(args[DEVICE_ID]) if args.get(DEVICE_ID) else args[SERIAL_PORT],
                      baudrate=args[BAUD_RATE],
                      debug=True):
        try:
            sleep()
        except KeyboardInterrupt:
            pass
        finally:
            stopped = True

    logger.info("Exiting...")

