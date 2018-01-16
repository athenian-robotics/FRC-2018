#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/heading_publisher.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python ~pi/git/FRC-2018/heading_publisher.py --mqtt localhost --mpt 1 --calib --cpt 2 --did 00FEBA85 --baud 115200 &> ~pi/git/FRC-2018/logs/heading_publisher.out &

# Arduino with 9-DOF DID is 955303432353 95530343235351A0E0A2
# Metro mini with 9-DOF DID is 00FEBA85