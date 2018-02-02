import arc852.cli_args  as cli
import arc852.opencv_defaults as defs
import cv2
#import rospy
from arc852.generic_filter import GenericFilter
from arc852.opencv_utils import BLUE, GREEN, RED
from arc852.opencv_utils import get_moment
#from geometry_msgs.msg import Point
#from geometry_msgs.msg import Vector3


class SingleObjectFilter(GenericFilter):
    args = [cli.so_topic, cli.bgr, cli.hsv_range, cli.minimum_pixels, cli.draw_contour,
            cli.draw_line, cli.draw_box, cli.vertical_lines, cli.horizontal_lines]

    def __init__(self, tracker, so_topic, *args, **kwargs):
        super(SingleObjectFilter, self).__init__(tracker, *args, **kwargs)
        self.contour = None
        self.area = None
        self.img_x, self.img_y = -1, -1
        self.height, self.width = None, None
        #self.__loc_pub = rospy.Publisher(so_topic + "/point", Point, queue_size=5)
        #self.__dim_pub = rospy.Publisher(so_topic + "/dimensions", Vector3, queue_size=5)

    def reset_data(self):
        self.img_x, self.img_y = -1, -1

    def process_image(self, image):
        self.contour = None
        self.reset_data()
        self.height, self.width = image.shape[:2]

        # Find the largest contour
        self.contours = self.contour_finder.get_max_contours(image, count=1)

        if self.contours is not None and len(self.contours) == 1:
            self.contour, self.area, self.img_x, self.img_y = get_moment(self.contours[0])

    def publish_data(self):
        # Write location if it is different from previous value written
        if self.img_x != self.prev_x or self.img_y != self.prev_y:
            # self.location_server.write_location(self.img_x, self.img_y, self.width, self.height, self.middle_inc)
            #point = Point()
            #point.x = self.img_x
            #point.y = self.img_y
            #point.z = 0
            #self.__loc_pub.publish(point)

            #dim = Vector3()
            #dim.x = self.width
            #dim.y = self.height
            #dim.z = self.middle_inc
            #self.__dim_pub.publish(dim)

            self.prev_x, self.prev_y = self.img_x, self.img_y

    def markup_image(self, image):
        mid_x, mid_y = self.width / 2, self.height / 2
        mid_inc = int(self.middle_inc)

        x_in_middle = mid_x - mid_inc <= self.img_x <= mid_x + mid_inc
        y_in_middle = mid_y - mid_inc <= self.img_y <= mid_y + mid_inc
        x_color = GREEN if x_in_middle else RED if self.img_x == -1 else BLUE
        y_color = GREEN if y_in_middle else RED if self.img_y == -1 else BLUE

        if not self.tracker.markup_image:
            return

        text = "#{0} ({1}, {2})".format(self.tracker.cnt, self.width, self.height)
        text += " {0}%".format(self.tracker.middle_percent)

        if self.contours is not None and len(self.contours) == 1:
            x, y, w, h = cv2.boundingRect(self.contour)
            if self.draw_box:
                cv2.rectangle(image, (x, y), (x + w, y + h), BLUE, 2)
            if self.draw_contour:
                cv2.drawContours(image, [self.contour], -1, GREEN, 2)
            cv2.circle(image, (self.img_x, self.img_y), 4, RED, -1)
            text += " ({0}, {1})".format(self.img_x, self.img_y)
            text += " {0}".format(self.area)

        # Draw the alignment lines
        if self.vertical_lines:
            cv2.line(image, (mid_x - mid_inc, 0), (mid_x - mid_inc, self.height), x_color, 1)
            cv2.line(image, (mid_x + mid_inc, 0), (mid_x + mid_inc, self.height), x_color, 1)

        if self.horizontal_lines:
            cv2.line(image, (0, mid_y - mid_inc), (self.width, mid_y - mid_inc), y_color, 1)
            cv2.line(image, (0, mid_y + mid_inc), (self.width, mid_y + mid_inc), y_color, 1)

        if self.display_text:
            cv2.putText(image, text, defs.TEXT_LOC, defs.TEXT_FONT, defs.TEXT_SIZE, RED, 1)
