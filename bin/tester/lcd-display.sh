#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/lcd_writer.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics

python3 ~pi/git/FRC-2017/lcd_writer.py --mqtt localhost &> ~pi/git/FRC-2017/logs/lcd_writer.out &
