#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/msg_logger.reboot
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
python ~pi/git/FRC-2017/msg_logger.py --mqtt localhost --dir ~pi/git/FRC-2017/logs &> ~pi/git/FRC-2017/logs/msg_logger.out &

