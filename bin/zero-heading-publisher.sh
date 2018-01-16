#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/heading_publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python ~pi/git/FRC-2017/heading_publisher.py --mqtt pleiku.local --mpt 1 --calib --cpt 2 --did 00FEBA85 --baud 115200 &> ~pi/git/FRC-2017/logs/heading_publisher.out &
