#!/usr/bin/env python

import argparse
import logging
from threading import Lock

import arc852.cli_args as cli
from arc852.constants import SERIAL_PORT, BAUD_RATE, MQTT_HOST, LOG_LEVEL, DEVICE_ID
from arc852.serial_reader import SerialReader
from arc852.utils import setup_logging
from arc852.utils import sleep

import frc_utils
from frc_utils import COMMAND
from frc_utils import ENABLED

import rospy
from std_msgs.msg import Int32

logger = logging.getLogger(__name__)

CALIBRATION_BY_VALUES = "9-DOF Sensor calibrated by values"
CALIBRATION_BY_LOG = "9-DOF Sensor calibrated by log"
HEADING_PUB = "heading_topic"
CALIB_PUB = "calib_topic"
HEADING_RATE = "heading_rate"
CALIB_RATE = "calib_rate"
CALIB_PUBLISH = "calib_publish"
CALIB_ENABLED = "calib_enabled"
MIN_PUBLISH = "min_publish"
PUBLISH_LOCK = "publish_lock"

stopped = False
calibrated_by_values = False
calibrated_by_log = False
last_heading_publish_time = -1
last_calib_publish_time = -1


# SerialReader calls this for every line read from Arduino
def fetch_data(val, userdata):
    global calibrated_by_values, calibrated_by_log, last_calib_publish_time

    if "X:" not in val:
        logger.info("Non-data: %s", val)
    else:
        try:
            vals = val.split("\t")

            x_val = vals[0]
            heading = round(float(x_val.split(": ")[1]), 1)

            logger.info(val)
            publish_heading(heading, userdata)

            if userdata[CALIB_ENABLED] and not calibrated_by_values:
                # The arduino sketch includes a "! " prefix to SYS if the data is not calibrated (and thus not reliable)
                if "! " in val:
                    nocalib_str = val[val.index("! "):]
                    logger.info("9-DOF Sensor not calibrated by log: %s", nocalib_str)
                    publish_calibration(nocalib_str, userdata)
                    calibrated_by_log = False
                else:
                    if not calibrated_by_log:
                        msg = CALIBRATION_BY_LOG
                        logger.info(msg)
                        publish_calibration(msg, userdata)
                        calibrated_by_log = True

                    calib_str = vals[3]
                    calibs = calib_str.split(" ")
                    sys_calib = int(calibs[0].split(":")[1])
                    gyro_calib = int(calibs[1].split(":")[1])
                    mag_calib = int(calibs[2].split(":")[1])
                    acc_calib = int(calibs[3].split(":")[1])

                    if sys_calib == 3 and gyro_calib == 3 and mag_calib == 3 and acc_calib == 3:
                        msg = CALIBRATION_BY_VALUES
                        logger.info(msg)
                        publish_calibration(msg, userdata)
                        calibrated_by_values = True
                    else:
                        publish_calibration(calib_str, userdata)
        except IndexError:
            logger.info("Formatting error: %s", val)


def publish_heading(heading, userdata):
    if not userdata[ENABLED]:
        return

    publish_lock = userdata[PUBLISH_LOCK]
    with publish_lock:
        userdata[HEADING_PUB].publish(heading)
        userdata[HEADING_RATE].sleep()


def publish_calibration(calibration, userdata):
    if not userdata[ENABLED]:
        return

    publish_lock = userdata[PUBLISH_LOCK]
    with publish_lock:
        userdata[CALIB_PUB].publish(calibration)
        userdata[CALIB_RATE].sleep()


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.device_id(parser)
    cli.serial_port(parser)
    cli.baud_rate(parser)
    parser.add_argument("--mpt", dest=MIN_PUBLISH, default=1, type=int, help="Minimum publishing time secs [1]")
    parser.add_argument("--calib", dest=CALIB_ENABLED, default=False, action="store_true",
                        help="Enable calibration publishing[false]")
    parser.add_argument("--cpt", dest=CALIB_PUBLISH, default=3, type=int, help="Calibration publishing time secs [3]")
    cli.verbose(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    rospy.init_node('imu_heading_publisher')
    heading_pub = rospy.Publisher("imu/degrees", Int32, queue_size=10)
    heading_rate = rospy.Rate(20)
    calib_pub = rospy.Publisher("imu/calibration", Int32, queue_size=10)
    calib_rate = rospy.Rate(1)

    userdata = {HEADING_PUB: heading_pub,
                CALIB_PUB: calib_pub,
                HEADING_RATE: heading_rate,
                CALIB_RATE: calib_rate,
                COMMAND: "imu/command",
                ENABLED: True,
                PUBLISH_LOCK: Lock(),
                CALIB_PUBLISH: args[CALIB_PUBLISH],
                CALIB_ENABLED: args[CALIB_ENABLED],
                MIN_PUBLISH: args[MIN_PUBLISH]},

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
