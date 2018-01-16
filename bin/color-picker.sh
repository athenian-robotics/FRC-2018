#!/usr/bin/env bash

source ~pi/.profile
workon py2cv3
date > ~pi/git/FRC-2017/logs/dualtape-peg-color-picker.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
~pi/git/object-tracking/color_picker.py --sleep 60 --usb --width 600 --flipy --http "127.0.0.1:8080" &> ~pi/git/FRC-2017/logs/color-picker.out &
