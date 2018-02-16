#!/usr/bin/env bash

su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_left_front_publisher.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_left_back_publisher.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_right_front_publisher.sh
su - pi -c /home/pi/catkin_ws/src/frc_2018_sensors/bin/lidar_right_back_publisher.sh