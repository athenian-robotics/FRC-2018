#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/lcd_writer.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

# Old
#python3 ~pi/git/FRC-2018/lidar_display.py --mqtt mqtt-turtle.local &> ~pi/git/FRC-2018/logs/lidar_display.out &

python3 ~pi/git/FRC-2018/lcd_writer.py --mqtt mqtt-turtle.local &> ~pi/git/FRC-2018/logs/lcd_writer.out &

# Testing
# python3 ~pi/git/FRC-2018/lcd_writer.py --mqtt pleiku.local &> ~pi/git/FRC-2018/logs/lcd_writer.out &

