#!/usr/bin/env bash

# Publish lidar data
su - pi -c ~pi/git/FRC-2017/bin/lidar-front-publisher.sh
su - pi -c ~pi/git/FRC-2017/bin/lidar-rear-publisher.sh

