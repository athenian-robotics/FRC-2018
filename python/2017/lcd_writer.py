#!/usr/bin/env python2

import logging
import time
from collections import deque
from threading import Thread

import arc852.cli_args as cli
import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav
from arc852.constants import MQTT_HOST, LOG_LEVEL
from arc852.mqtt_connection import MqttConnection
from arc852.utils import setup_logging, waitForKeyboardInterrupt

from heading_publisher import CALIBRATION_BY_VALUES

logger = logging.getLogger(__name__)

ITEM_DICT = "ITEM_DICT"

# Constants
LIDAR_LEFT_TOPIC = "lidar/left/mm"
LIDAR_RIGHT_TOPIC = "lidar/right/mm"
LIDAR_FRONT_TOPIC = "lidar/front/cm"
LIDAR_REAR_TOPIC = "lidar/rear/cm"
CAMERA_VALUE_TOPIC = "camera/gear/x"
HEADING_CALIBRATION_TOPIC = "heading/calibration"
HEADING_DEGREES_TOPIC = "heading/degrees"
METRICS_TOPIC = "metrics/msg_rate"

NOT_SEEN = "not_seen"
NOT_ALIGNED = "not_aligned"
ALIGNED = "aligned"


class LcdItem(object):
    def __init__(self, topic, desc):
        self.topic = topic
        self.desc = desc
        self.value = ""


items = [LcdItem(LIDAR_LEFT_TOPIC, "Lidar Left", ),
         LcdItem(LIDAR_RIGHT_TOPIC, "Lidar Right"),
         LcdItem(LIDAR_FRONT_TOPIC, "Lidar Front"),
         LcdItem(LIDAR_REAR_TOPIC, "Lidar Rear"),
         LcdItem(CAMERA_VALUE_TOPIC, "Camera"),
         LcdItem(HEADING_CALIBRATION_TOPIC, "Calibration"),
         LcdItem(HEADING_DEGREES_TOPIC, "Degrees"),
         LcdItem(METRICS_TOPIC, "Msgs/Sec")]

item_dict = {}
for i in items:
    item_dict[i.topic] = i

item_deque = deque()
for i in item_dict.keys():
    item_deque.append(item_dict[i])

# default sensor
selected_sensor = item_deque[0]

# lcd initialization
lcd.clear()
backlight.rgb(255, 255, 255)
lcd.set_contrast(45)
lcd.clear()


def on_connect(mqtt_client, userdata, flags, rc):
    logger.info("Connected with result code: %s", rc)

    item_dict = userdata[ITEM_DICT]
    for key in item_dict.keys():
        mqtt_client.subscribe(item_dict[key].topic)


def on_message(mqtt_client, userdata, msg):
    item_dict = userdata[ITEM_DICT]

    # Payload is a string byte array
    val = bytes.decode(msg.payload)
    logger.info("%s : %s", msg.topic, val)

    item = item_dict[msg.topic]
    if item is None:
        logger.warn("Invalid topic: %s", msg.topic)
        return

    logger.info("%s: %s", msg.topic, val)
    item.value = val


def lcd_display(dict, delay=0.1):
    while True:
        try:
            lcd.clear()
            lcd.set_cursor_position(0, 0)
            lcd.write(selected_sensor.desc)
            lcd.set_cursor_position(0, 2)

            val = selected_sensor.value
            if val == "-1":
                backlight.rgb(255, 0, 0)
            else:
                backlight.rgb(255, 255, 255)

            if selected_sensor == dict[LIDAR_LEFT_TOPIC]:
                lcd.write(val + " mm")

            elif selected_sensor == dict[LIDAR_RIGHT_TOPIC]:
                lcd.write(val + " mm")

            elif selected_sensor == dict[LIDAR_FRONT_TOPIC]:
                lcd.write(val + " cm")

            elif selected_sensor == dict[LIDAR_REAR_TOPIC]:
                lcd.write(val + " cm")

            elif selected_sensor == dict[CAMERA_VALUE_TOPIC]:
                lcd.write(val)
                if val == NOT_SEEN:
                    backlight.rgb(255, 0, 0)
                elif val == NOT_ALIGNED:
                    backlight.rgb(0, 0, 255)
                elif val == ALIGNED:
                    backlight.rgb(0, 255, 0)

            elif selected_sensor == dict[HEADING_CALIBRATION_TOPIC]:
                lcd.write(val.replace(" ", "", 10))
                if val == CALIBRATION_BY_VALUES:
                    backlight.rgb(0, 255, 0)

            elif selected_sensor == dict[HEADING_DEGREES_TOPIC]:
                lcd.write(val)

            elif selected_sensor == dict[METRICS_TOPIC]:
                lcd.write(val)

            else:
                lcd.write("")

            time.sleep(delay)

        except BaseException as e:
            logger.error("%s", e, exc_info=True)
            time.sleep(1)


def assign_selected_sensor():
    global selected_sensor
    selected_sensor = item_deque[0]
    logger.info(selected_sensor.desc)
    lcd.clear()
    backlight.rgb(255, 255, 255)
    lcd.set_cursor_position(0, 0)
    lcd.write(selected_sensor.desc)
    lcd.set_cursor_position(0, 2)


@nav.on(nav.UP)
def handle_up_button(ch, evt):
    item_deque.rotate(1)
    assign_selected_sensor()


@nav.on(nav.DOWN)
def handle_down_button(ch, evt):
    item_deque.rotate(-1)
    assign_selected_sensor()


if __name__ == "__main__":
    # Parse CLI args
    args = cli.setup_cli_args(cli.mqtt_host, cli.log_level())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    Thread(target=lcd_display, args=(item_dict, 0.1)).start()

    # Setup MQTT client
    with MqttConnection(args[MQTT_HOST],
                        userdata={ITEM_DICT: item_dict},
                        on_connect=on_connect,
                        on_message=on_message):
        waitForKeyboardInterrupt()

    logger.info("Exiting...")
