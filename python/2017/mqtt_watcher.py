#!/usr/bin/env python3

import argparse
import logging

import arc852.cli_args as cli
from arc852.constants import MQTT_HOST, TOPIC, MQTT_TOPIC
from arc852.mqtt_connection import MqttConnection
from arc852.utils import setup_logging, waitForKeyboardInterrupt

logger = logging.getLogger(__name__)


def on_connect(mqtt_client, userdata, flags, rc):
    logging.info("Connected with result code: %s", rc)
    # Subscribe to all broker messages
    mqtt_client.subscribe(userdata[TOPIC])


def on_message(mqtt_client, userdata, msg):
    logger.info("%s : %s", msg.topic, msg.payload)


if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.mqtt_topic(parser)
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging()

    with MqttConnection(args[MQTT_HOST],
                        userdata={TOPIC: args[MQTT_TOPIC]},
                        on_connect=on_connect,
                        on_message=on_message):
        waitForKeyboardInterrupt()

    logger.info("Exiting...")
