#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/snap_motion_server.reboot
export PYTHONWARNINGS="ignore"
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python ~pi/git/distance-tracking/snap_motion_server.py --did 00FEBA85 --baud 115200 &> ~pi/git/FRC-2018/logs/snap_motion_server.out &

