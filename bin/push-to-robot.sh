#!/usr/bin/env bash

# Push common-robotics repo
echo "Pushing common-robotics to robot"
cd ~/git/common-robotics
git push camera-gear master
git push camera-rope master
git push lidar-gear master
git push lcd1 master

# Push FRC-2017 repo
echo "Pushing FRC-2017 to robot"
cd ~/git/FRC-2017
git push camera-gear master
git push camera-rope master
git push lidar-gear master
git push lcd1 master

# Push object-tracking repo
echo "Pushing object-tracking to robot"
cd ~/git/object-tracking
git push camera-gear master
git push camera-rope master


