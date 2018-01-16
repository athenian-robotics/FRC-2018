#!/usr/bin/env bash

# Push common-robotics repo
echo "Updating common-robotics"
cd ~/git/common-robotics
git pull origin

# Push FRC-2017 repo
echo "Updating FRC-2017"
cd ~/git/FRC-2017
git pull origin

# Push object-tracking repo
echo "Updating object-tracking"
cd ~/git/object-tracking
git pull origin

# Push FRC-2017-robot repo
echo "Updating FRC-2017-robot"
cd ~/git/FRC-2017-robot
git pull origin


