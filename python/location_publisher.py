#!/usr/bin/env python2

import logging
import time
from threading import Thread

import cli_args as cli
from cli_args import setup_cli_args
from constants import MQTT_HOST, LOG_LEVEL, GRPC_HOST, TOPIC, MQTT_TOPIC
from location_client import LocationClient
from mqtt_connection import MqttConnection
from utils import setup_logging, waitForKeyboardInterrupt

import frc_utils
from frc_utils import COMMAND, ENABLED

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Parse CLI args
    args = setup_cli_args(cli.grpc_host, cli.mqtt_host, cli.mqtt_topic, cli.verbose)

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    # Start location reader
    with LocationClient(args[GRPC_HOST]) as loc_client:

        # Define MQTT callbacks
        def on_connect(mqtt_client, userdata, flags, rc):
            logger.info("Connected to MQTT broker with result code: %s", rc)
            Thread(target=publish_locations, args=(mqtt_client, userdata)).start()
            mqtt_client.subscribe(userdata[COMMAND])


        def publish_locations(mqtt_client, userdata):
            prev_value = -1
            while True:
                try:
                    x_loc = loc_client.get_x()

                    if not userdata[ENABLED]:
                        continue

                    if x_loc is not None and abs(x_loc[0] - prev_value) > 1:
                        result, mid = mqtt_client.publish("{0}/x".format(userdata[TOPIC]),
                                                          payload="{0}:{1}".format(x_loc[0], x_loc[1]).encode('utf-8'))
                        prev_value = x_loc[0]

                except BaseException as e:
                    logger.error("Failure in publish_locations() [%s]", e, exc_info=True)
                    time.sleep(1)


        # Setup MQTT client
        with MqttConnection(args[MQTT_HOST],
                            userdata={TOPIC: args[MQTT_TOPIC],
                                      COMMAND: args[MQTT_TOPIC] + "/command",
                                      ENABLED: True},
                            on_connect=on_connect,
                            on_message=frc_utils.on_message):
            waitForKeyboardInterrupt()

    logger.info("Exiting...")
