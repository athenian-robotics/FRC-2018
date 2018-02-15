import arc852.cli_args  as cli
import arc852.opencv_defaults as defs
import cv2
from arc852.constants import MAXIMUM_OBJECTS_DEFAULT
from arc852.generic_filter import GenericFilter
from arc852.opencv_utils import BLUE, GREEN, RED
from arc852.opencv_utils import get_moment
from matplotlib.pylab import polyfit


class MultiObjectFilter(GenericFilter):
    args = [cli.so_topic, cli.bgr, cli.hsv_range, cli.minimum_pixels,
            cli.draw_line, cli.draw_contour, cli.draw_box, cli.max_objects]

    def __init__(self, tracker, so_topic, maximum_objects=MAXIMUM_OBJECTS_DEFAULT,
                 *args, **kwargs):
        super(MultiObjectFilter, self).__init__(tracker, *args, **kwargs)
        self.__max_objects = maximum_objects
        self.__moments = None
        self.__contours = None
        self.__height, self.__width = None, None

    def reset_data(self):
        self.__moments = []
        self.__contours = None

    def process_image(self, image):
        self.reset_data()
        self.__height, self.__width = image.shape[:2]
        self.__contours = self.contour_finder.get_max_contours(image, count=self.__max_objects)
        if self.__contours is not None:
            self.__moments = [get_moment(i) for i in self.__contours]

    def publish_data(self):
        # Write location if it is different from previous value written
        # if self.avg_x != self.prev_x or self.avg_y != self.prev_y:
        # self.location_server.write_location(self.avg_x, self.avg_y, self.width, self.height, self.middle_inc)
        #    self.prev_x, self.prev_y = self.avg_x, self.avg_y
        pass

    def markup_image(self, image):
        if not self.tracker.markup_image:
            return

        text = "#{0} ({1}, {2})".format(self.tracker.cnt, self.__width, self.__height)
        text += " {0}%".format(self.tracker.middle_percent)

        if self.__contours is not None:
            all_x = []
            all_y = []
            for i in range(len(self.__contours)):
                box_x, box_y, box_w, box_h = cv2.boundingRect(self.__contours[i])
                center_x = self.__moments[i][2]
                center_y = self.__moments[i][3]
                all_x.append(center_x)
                all_y.append(center_y)

                if self.draw_box:
                    cv2.rectangle(image, (box_x, box_y), (box_x + box_w, box_y + box_h), BLUE, 2)

                if self.draw_contour:
                    cv2.drawContours(image, [self.__contours[i]], -1, GREEN, 2)

                # Draw center
                cv2.circle(image, (center_x, center_y), 4, RED, -1)
                # text += " Avg: ({0}, {1})".format(self.avg_x, self.avg_y)

            if self.draw_line and len(all_x) >= 2:
                m, b = polyfit(all_x, all_y, 1)
                cv2.line(image, (0, int(b)), (self.__width, int((self.__width * m) + b)), BLUE, 2)

        # Draw the alignment lines
        # if self.vertical_lines:
        #    cv2.line(image, (mid_x - mid_inc, 0), (mid_x - mid_inc, self.height), x_color, 1)
        #    cv2.line(image, (mid_x + mid_inc, 0), (mid_x + mid_inc, self.height), x_color, 1)

        # if self.horizontal_lines:
        #    cv2.line(image, (0, mid_y - mid_inc), (self.width, mid_y - mid_inc), y_color, 1)
        #    cv2.line(image, (0, mid_y + mid_inc), (self.width, mid_y + mid_inc), y_color, 1)

        if self.display_text:
            cv2.putText(image, text, defs.TEXT_LOC, defs.TEXT_FONT, defs.TEXT_SIZE, RED, 1)
