#!/usr/bin/env bash

# Push common-robotics repo
echo "Pushing common-robotics to github"
cd ~/git/common-robotics
git push origin master

# Push FRC-2018 repo
echo "Pushing FRC-2018 to github"
cd ~/git/FRC-2018
git push origin master

# Push object-tracking repo
echo "Pushing object-tracking to github"
cd ~/git/object-tracking
git push origin master


