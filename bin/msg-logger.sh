#!/usr/bin/env bash

date > ~pi/git/FRC-2018/logs/msg_logger.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python ~pi/git/FRC-2018/msg_logger.py --mqtt mqtt-turtle.local --dir ~pi/git/FRC-2018/logs &> ~pi/git/FRC-2018/logs/msg_logger.out &

