#!/usr/bin/env bash

source ~pi/.profile
workon py2cv3
date > ~pi/git/FRC-2018/logs/rope-publisher.reboot
#export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
python2 ~pi/git/FRC-2018/location_publisher.py --grpc camera-rope.local --topic camera/rope --mqtt mqtt-turtle.local &> ~pi/git/FRC-2018/logs/rope-publisher.out &

