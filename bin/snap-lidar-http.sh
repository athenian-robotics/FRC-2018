#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/snap-lidar-http.reboot
export PYTHONWARNINGS="ignore"
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python ~pi/git/distance-tracking/snap_distance_server.py --did 00FEBABC --baud 115200 &> ~pi/git/FRC-2018/logs/snap_distance_server.out &

