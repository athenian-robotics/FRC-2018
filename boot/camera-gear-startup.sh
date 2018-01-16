#!/usr/bin/env bash

# Tune exposure on camera
v4l2-ctl -d /dev/video0 -c exposure_auto=1 -c exposure_absolute=20

# We have two configurations: object tracking and color picking
# They both need exclusive camera access, so if one of the two is enabled,
# the other needs to be commented out.

# Object tracking
su - pi -c ~pi/git/FRC-2017/bin/dual-tape-tracker.sh

#su - pi -c ~pi/git/FRC-2017/bin/dual-tape-peg-tracker.sh

# MQTT publishing
su - pi -c ~pi/git/FRC-2017/bin/gear-front-publisher.sh

# Color picking
#su - pi -c ~pi/git/FRC-2017/bin/color-picker.sh
