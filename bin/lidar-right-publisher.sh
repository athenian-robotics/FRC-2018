#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/lidar-right-publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python3 ~pi/git/FRC-2018/short_lidar_publisher.py --mqtt mqtt-turtle.local --device right --did 95538333535351019130 --baud 115200  --oor_size 5 --oor_time 1000 --oor_upper 2000 &> ~pi/git/FRC-2018/logs/lidar-right-publisher.out &
