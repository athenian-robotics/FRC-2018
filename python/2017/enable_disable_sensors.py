import argparse
import logging
import time
from threading import Thread

import cli_args as cli
from constants import MQTT_HOST
from mqtt_connection import MqttConnection
from utils import waitForKeyboardInterrupt

logger = logging.getLogger(__name__)

cmds = ["lidar/left/command", "lidar/right/command",
        "lidar/front/command", "lidar/rear/command",
        "heading/command",
        "camera/gear/command"]

if __name__ == "__main__":
    def on_connect(mqtt_client, userdata, flags, rc):
        logger.info("Connected with result code: %s", rc)
        Thread(target=enable_disable, args=(mqtt_client,)).start()


    def enable_disable(client):
        while True:
            for i in cmds:
                client.publish(i, payload="OFF", qos=0)
            time.sleep(3)
            for i in cmds:
                client.publish(i, payload="ON", qos=0)
            time.sleep(10)


    # Parse CLI args
    parser = argparse.ArgumentParser()
    cli.mqtt_host(parser)
    cli.verbose(parser)
    args = vars(parser.parse_args())

    with MqttConnection(hostname=args[MQTT_HOST],
                        userdata={},
                        on_connect=on_connect):
        waitForKeyboardInterrupt()

    logger.info("Exiting...")
