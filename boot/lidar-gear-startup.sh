#!/usr/bin/env bash

# Publish short lidar data
su - pi -c ~pi/git/FRC-2017/bin/lidar-right-publisher.sh
su - pi -c ~pi/git/FRC-2017/bin/lidar-left-publisher.sh

# Publish heading data
#su - pi -c ~pi/git/FRC-2017/bin/heading-publisher.sh

# Publish long lidar data
su - pi -c ~pi/git/FRC-2017/bin/lidar-front-publisher.sh
su - pi -c ~pi/git/FRC-2017/bin/lidar-rear-publisher.sh
