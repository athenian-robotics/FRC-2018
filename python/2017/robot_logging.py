#!/usr/bin/env python3

import argparse
import logging

import arc852.cli_args as cli
from arc852.constants import MQTT_HOST, LOG_FILE, MQTT_TOPIC, TOPIC
from arc852.mqtt_connection import MqttConnection
from arc852.utils import setup_logging, waitForKeyboardInterrupt

logger = logging.getLogger(__name__)


def on_connect(mqtt_client, userdata, flags, rc):
    # Subscribe to all broker messages
    topic = userdata[TOPIC]
    mqtt_client.subscribe(topic)
    setup_logging(filename=args[LOG_FILE],
                  format="%(asctime)s %(levelname)-6s %(message)s",
                  level=logging.DEBUG)
    logger.info("Connected, subscribing to topic %s", topic)
    # print("Connected, subscribing to topic {0}".format(topic))


def on_message(mqtt_client, userdata, msg):
    logger.info("%s : %s", msg.topic, msg.payload)
    # print("{0} : {1}".format(msg.topic, msg.payload))


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.log_file(parser)
    cli.mqtt_topic(parser)
    args = vars(parser.parse_args())

    with MqttConnection(args[MQTT_HOST],
                        userdata={TOPIC: args[MQTT_TOPIC]},
                        on_connect=on_connect,
                        on_message=on_message):
        waitForKeyboardInterrupt()

    logger.info("Exiting...")
