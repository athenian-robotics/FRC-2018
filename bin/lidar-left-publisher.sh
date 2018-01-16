#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/lidar-left-publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python3 ~pi/git/FRC-2018/short_lidar_publisher.py --mqtt mqtt-turtle.local --device left --did 7543331373935160E190 --baud 115200 --oor_size 5 --oor_time 1000 --oor_upper 2000 &> ~pi/git/FRC-2018/logs/lidar-left-publisher.out &
