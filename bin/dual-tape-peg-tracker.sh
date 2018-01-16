#!/usr/bin/env bash

source ~pi/.profile
workon py2cv3
date > ~pi/git/FRC-2017/logs/dual-tape-peg-tracker.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
python2 ~pi/git/object-tracking/multi_object_tracker.py --mask_x 0 --dualbgr "172, 220, 14" --singlebgr "126, 113, 116" --draw_contour --draw_box --sleep 90 --width 500 --delay 0.25 --flipy --usb --http "127.0.0.1:8080" --vertical &> ~pi/git/FRC-2017/logs/dual-tape-peg-tracker.out &


# 174, 56, 5 is blue
# 46, 43, 144 is red box