#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/lidar-front-publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python3 ~pi/git/FRC-2017/long_lidar_publisher.py --mqtt localhost --avg_size 20 --device front --did 00FEBA8B --baud 115200 &> ~pi/git/FRC-2017/logs/lidar-front-publisher.out &
