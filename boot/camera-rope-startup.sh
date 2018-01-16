#!/usr/bin/env bash

# Publish heading data
su - pi -c ~pi/git/FRC-2017/bin/heading-publisher.sh

su - pi -c ~pi/git/FRC-2017/bin/rope-tracker.sh
#su - pi -c ~pi/git/FRC-2017/bin/rope-publisher.sh

su - pi -c ~pi/git/FRC-2017/bin/msg-logger.sh

su - pi -c ~pi/git/FRC-2017/bin/system-metrics.sh

