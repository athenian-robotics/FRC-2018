#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/lidar-left-publisher.reboot
#export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python3 ~pi/git/FRC-2018/short_lidar_publisher.py --mqtt localhost --device left --did 00FEBABC --baud 115200 --oor_size 5 --oor_time 1000 --oor_upper 2000 &> ~pi/git/FRC-2018/logs/lidar-left-publisher.out &
