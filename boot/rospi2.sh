#!/usr/bin/env bash

su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lcd_display.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/imu_publisher.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_front_publisher.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_back_publisher.sh