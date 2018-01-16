#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/lidar-rear-publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python3 ~pi/git/FRC-2017/long_lidar_publisher.py --mqtt mqtt-turtle.local --avg_size 20 --device rear --did 00FEBA73 --baud 115200 &> ~pi/git/FRC-2017/logs/lidar-rear-publisher.out &

# Testing
# python3 ~pi/git/FRC-2017/long_lidar_publisher.py --mqtt pleiku.local --avg_size 20 --device rear --did 00FEBA73 --baud 115200 &> ~pi/git/FRC-2017/logs/lidar-rear-publisher.out &
