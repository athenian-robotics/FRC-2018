#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/system_metrics.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python ~pi/git/FRC-2017/system_metrics.py --mqtt mqtt-turtle.local &> ~pi/git/FRC-2017/logs/system_metrics.out &

