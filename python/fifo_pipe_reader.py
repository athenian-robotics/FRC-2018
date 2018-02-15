#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno
import logging
import os
import sys
from threading import Thread

import arc852.cli_args  as cli
from arc852.cli_args import LOG_LEVEL
from arc852.cli_args import setup_cli_args
from arc852.constants import HTTP_DELAY_SECS, TEMPLATE_FILE, HTTP_VERBOSE, IMAGE_X, IMAGE_Y
from arc852.constants import HTTP_PORT, CAMERA_NAME
from arc852.image_server_nohost import ImageServer
from arc852.utils import setup_logging, sleep

logger = logging.getLogger(__name__)

FIFO_NAME = "fifo_name"
FIFO_VERBOSE = "fifo_verbose"


def fifo_name_option(p):
    return p.add_argument("-f", "--fifo", dest=FIFO_NAME, required=True, help="FIFO pipe name")


def fifo_verbose(p):
    return p.add_argument("--fifo_verbose", dest=FIFO_VERBOSE, default=False, action="store_true",
                          help="FIFO verbose [false]")


class FifoReader(object):
    def __init__(self, image_server, fifo_name, fifo_verbose=False):
        self.__image_server = image_server
        self.__fifo_name = fifo_name
        self.__fifo_verbose = fifo_verbose
        self.__stopped = False

    def read_fifo(self, image_server):
        while not self.__stopped:
            if self.__fifo_verbose:
                logger.info("Opening FIFO...")
            with open(self.__fifo_name) as fifo:
                if self.__fifo_verbose:
                    logger.info("FIFO opened")
                while not self.__stopped:
                    data = fifo.read()
                    if len(data) == 0:
                        break
                    image_server.image = data

    def start(self):
        # Make sure named pip exists. If not create it.
        try:
            os.mkfifo(self.__fifo_name)
        except OSError as oe:
            if oe.errno != errno.EEXIST:
                raise

        logger.info("Starting FIFO reader...")
        fifo_thread = Thread(target=self.read_fifo, kwargs={"image_server": self.__image_server})
        logger.info("Started FIFO reader")
        fifo_thread.start()

    def stop(self):
        self.__stopped = True


def main():
    # Parse CLI args
    args = setup_cli_args(ImageServer.args,
                          cli.camera_name_optional,
                          fifo_name_option,
                          fifo_verbose,
                          cli.log_level)

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    image_server = ImageServer(template_file=args[TEMPLATE_FILE],
                               image_x=args[IMAGE_X],
                               image_y=args[IMAGE_Y],
                               camera_name=args[CAMERA_NAME],
                               http_port=args[HTTP_PORT],
                               http_delay_secs=args[HTTP_DELAY_SECS],
                               http_verbose=args[HTTP_VERBOSE])
    fifo_reader = FifoReader(image_server=image_server, fifo_name=args[FIFO_NAME], fifo_verbose=args[FIFO_VERBOSE])

    try:
        image_server.start()
        fifo_reader.start()
        sleep()
    except KeyboardInterrupt:
        pass
    finally:
        image_server.stop()
        fifo_reader.stop()

    logger.info("Exiting")
    sys.exit(1)


if __name__ == "__main__":
    main()
