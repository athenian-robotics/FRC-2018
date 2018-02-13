#!/usr/bin/env python

import logging

import arc852.cli_args  as cli
from arc852.camera_image_source import CameraImageSource
from arc852.cli_args import LOG_LEVEL
from arc852.cli_args import setup_cli_args
from arc852.constants import DISPLAY, WIDTH, MIDDLE_PERCENT
from arc852.constants import DRAW_LINE, DRAW_CONTOUR, DRAW_BOX, VERTICAL_LINES, HORIZONTAL_LINES
from arc852.constants import FLIP_X, FLIP_Y, HTTP_DELAY_SECS, HTTP_FILE, HTTP_VERBOSE
from arc852.constants import MASK_X, MASK_Y, USB_PORT, BGR_COLOR
from arc852.constants import MINIMUM_PIXELS, HSV_RANGE, CAMERA_NAME, USB_CAMERA, HTTP_HOST, SO_TOPIC
from arc852.image_server import ImageServer
from arc852.object_tracker import ObjectTracker
from arc852.utils import setup_logging

from single_object_filter import SingleObjectFilter

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Parse CLI args
    args = setup_cli_args(CameraImageSource.args,
                          ImageServer.args,
                          cli.camera_name_optional,
                          SingleObjectFilter.args,
                          ObjectTracker.args,
                          cli.log_level)

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    image_source = CameraImageSource(usb_camera=args[USB_CAMERA], usb_port=args[USB_PORT])

    image_server = ImageServer(template_file=args[HTTP_FILE],
                               camera_name=args[CAMERA_NAME],
                               http_host=args[HTTP_HOST],
                               http_delay_secs=args[HTTP_DELAY_SECS],
                               http_verbose=args[HTTP_VERBOSE])

    tracker = ObjectTracker(image_source=image_source,
                            image_server=image_server,
                            width=args[WIDTH],
                            middle_percent=args[MIDDLE_PERCENT],
                            display=args[DISPLAY],
                            flip_x=args[FLIP_X],
                            flip_y=args[FLIP_Y],
                            mask_x=args[MASK_X],
                            mask_y=args[MASK_Y])

    obj_filter = SingleObjectFilter(tracker=tracker,
                                    so_topic=args[SO_TOPIC],
                                    bgr_color=args[BGR_COLOR],
                                    hsv_range=args[HSV_RANGE],
                                    minimum_pixels=args[MINIMUM_PIXELS],
                                    display_text=True,
                                    draw_line=args[DRAW_LINE],
                                    draw_contour=args[DRAW_CONTOUR],
                                    draw_box=args[DRAW_BOX],
                                    vertical_lines=args[VERTICAL_LINES],
                                    horizontal_lines=args[HORIZONTAL_LINES])
    try:
        image_source.start()
        image_server.start()
        tracker.run(obj_filter)
    except KeyboardInterrupt:
        pass
    finally:
        tracker.cleanup()
        image_server.stop()
        image_source.stop()

    logger.info("Exiting")
