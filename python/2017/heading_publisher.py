#!/usr/bin/env python

import argparse
import logging
import time
from threading import Lock
from threading import Thread

import arc852.cli_args as cli
from arc852.constants import SERIAL_PORT, BAUD_RATE, MQTT_HOST, LOG_LEVEL, DEVICE_ID
from arc852.mqtt_connection import MqttConnection, PAHO_CLIENT
from arc852.serial_reader import SerialReader
from arc852.utils import current_time_millis
from arc852.utils import setup_logging
from arc852.utils import sleep

import frc_utils
from frc_utils import COMMAND
from frc_utils import ENABLED

logger = logging.getLogger(__name__)

CALIBRATION_BY_VALUES = "9-DOF Sensor calibrated by values"
CALIBRATION_BY_LOG = "9-DOF Sensor calibrated by log"
HEADING_TOPIC = "heading_topic"
CALIB_TOPIC = "calib_topic"
CALIB_PUBLISH = "calib_publish"
CALIB_ENABLED = "calib_enabled"
MIN_PUBLISH = "min_publish"
PUBLISH_LOCK = "publish_lock"

stopped = False
calibrated_by_values = False
calibrated_by_log = False
current_heading = -1
last_heading_publish_time = -1
last_calib_publish_time = -1


def on_connect(mqtt_client, userdata, flags, rc):
    logger.info("Connected with result code: %s", rc)
    Thread(target=background_publisher, args=(userdata, userdata[MIN_PUBLISH])).start()
    mqtt_client.subscribe(userdata[COMMAND])


# SerialReader calls this for every line read from Arduino
def fetch_data(val, userdata):
    global current_heading, calibrated_by_values, calibrated_by_log, last_calib_publish_time

    if "X:" not in val:
        logger.info("Non-data: %s", val)
    else:
        try:
            mqtt_client = userdata[PAHO_CLIENT]
            vals = val.split("\t")

            x_val = vals[0]
            heading = round(float(x_val.split(": ")[1]), 1)
            if heading != current_heading:
                logger.debug(val)
                current_heading = heading
                publish_heading(mqtt_client, userdata[HEADING_TOPIC], heading, userdata)

            if userdata[CALIB_ENABLED] and not calibrated_by_values:
                # The arduino sketch includes a "! " prefix to SYS if the data is not calibrated (and thus not reliable)
                if "! " in val:
                    nocalib_str = val[val.index("! "):]
                    logger.info("9-DOF Sensor not calibrated by log: %s", nocalib_str)
                    mqtt_client.publish(userdata[CALIB_TOPIC], payload=(nocalib_str.encode("utf-8")), qos=0)
                    calibrated_by_log = False
                else:
                    if not calibrated_by_log:
                        msg = CALIBRATION_BY_LOG
                        logger.info(msg)
                        mqtt_client.publish(userdata[CALIB_TOPIC], payload=(msg.encode("utf-8")), qos=0)
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
                        mqtt_client.publish(userdata[CALIB_TOPIC], payload=(msg.encode("utf-8")), qos=0)
                        calibrated_by_values = True
                    elif current_time_millis() - last_calib_publish_time > userdata[CALIB_PUBLISH] * 1000:
                        mqtt_client.publish(userdata[CALIB_TOPIC], payload=(calib_str.encode("utf-8")), qos=0)
                        last_calib_publish_time = current_time_millis()
        except IndexError:
            logger.info("Formatting error: %s", val)


def background_publisher(userdata, min_publish_secs):
    client = userdata[PAHO_CLIENT]
    heading_topic = userdata[HEADING_TOPIC]
    while not stopped:
        time.sleep(.5)
        elapsed_time = current_time_millis() - last_heading_publish_time
        if elapsed_time > min_publish_secs * 1000 and current_heading != -1:
            publish_heading(client, heading_topic, current_heading, userdata)


def publish_heading(client, topic, heading, userdata):
    global last_heading_publish_time

    if not userdata[ENABLED]:
        return

    elapsed_time = current_time_millis() - last_heading_publish_time
    if elapsed_time < 75:
        return

    publish_lock = userdata[PUBLISH_LOCK]
    with publish_lock:
        client.publish(topic, payload=(str(heading).encode("utf-8")), qos=0)
        last_heading_publish_time = current_time_millis()


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.device_id(parser)
    cli.serial_port(parser)
    cli.baud_rate(parser)
    parser.add_argument("--mpt", dest=MIN_PUBLISH, default=1, type=int, help="Minimum publishing time secs [1]")
    parser.add_argument("--calib", dest=CALIB_ENABLED, default=False, action="store_true",
                        help="Enable calibration publishing[false]")
    parser.add_argument("--cpt", dest=CALIB_PUBLISH, default=3, type=int, help="Calibration publishing time secs [3]")
    cli.log_level(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    userdata = {HEADING_TOPIC: "heading/degrees",
                CALIB_TOPIC: "heading/calibration",
                COMMAND: "heading/command",
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
        with MqttConnection(hostname=(args[MQTT_HOST]),
                            userdata=userdata,
                            on_connect=on_connect,
                            on_message=frc_utils.on_message):
            try:
                sleep()
            except KeyboardInterrupt:
                pass
            finally:
                stopped = True

    logger.info("Exiting...")
