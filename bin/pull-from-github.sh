#!/usr/bin/env bash

# Push common-robotics repo
echo "Updating common-robotics"
cd ~/git/common-robotics
git pull origin

# Push FRC-2018 repo
echo "Updating FRC-2018"
cd ~/git/FRC-2018
git pull origin

# Push object-tracking repo
echo "Updating object-tracking"
cd ~/git/object-tracking
git pull origin

# Push FRC-2018-robot repo
echo "Updating FRC-2018-robot"
cd ~/git/FRC-2018-robot
git pull origin


