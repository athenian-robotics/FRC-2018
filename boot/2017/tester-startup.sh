#!/usr/bin/env bash

su - pi -c ~pi/git/FRC-2018/bin/tester/lcd-display.sh
su - pi -c ~pi/git/FRC-2018/bin/tester/system-metrics.sh
su - pi -c ~pi/git/FRC-2018/bin/tester/heading-publisher.sh
su - pi -c ~pi/git/FRC-2018/bin/tester/lidar-front-publisher.sh
su - pi -c ~pi/git/FRC-2018/bin/tester/lidar-rear-publisher.sh
su - pi -c ~pi/git/FRC-2018/bin/tester/lidar-left-publisher.sh


#su - pi -c ~pi/git/FRC-2018/bin/tester/msg-logger.sh
