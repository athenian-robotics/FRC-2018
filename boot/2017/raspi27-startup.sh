#!/usr/bin/env bash

# We have two configurations: object tracking and color picking
# They both need exclusive camera access, so if one of the two is enabled,
# the other needs to be commented out.

# Object tracking
su - pi -c ~pi/git/FRC-2018/bin/picamera-object-tracker.sh

# MQTT publishing
#su - pi -c ~pi/git/FRC-2018/bin/gear-front-publisher.sh

