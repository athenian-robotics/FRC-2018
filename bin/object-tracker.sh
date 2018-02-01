#!/usr/bin/env bash

source ~pi/.profile
workon py2cv3
date > ~pi/git/FRC-2018/logs/object-tracker.reboot
#export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
python2 ~pi/git/object-tracking/single_object_filter.py --bgr "174, 56, 5" --width 400 --delay 0.25 --flipy --usb --camera "Zero Camera" --http "raspi27.local:8080" --vertical &> ~pi/git/FRC-2018/logs/object-tracker.out &

# 59, 66, 197 is orange
# 174, 56, 5 is blue
# 46, 43, 144 is red box