import logging

SERIAL_READER = "serial_reader"
MOVING_AVERAGE = "moving_average"
DEVICE = "device"
AVG_SIZE = "avg_size"
ENABLED = "enabled"
COMMAND = "command"
OOR_VALUES = "oor_values"

OUT_OF_RANGE = "-1".encode("utf-8")

ENABLED_VALS = ["ON", "ENABLED", "YES", "1", "TRUE"]

logger = logging.getLogger(__name__)


def on_message(mqtt_client, userdata, msg):
    if msg.topic == userdata[COMMAND]:
        val = msg.payload.decode('ASCII').upper()
        is_enabled = val in ENABLED_VALS
        logger.info("With %s setting %s = %s", val, userdata[COMMAND], is_enabled)
        userdata[ENABLED] = is_enabled
