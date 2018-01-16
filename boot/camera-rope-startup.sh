#!/usr/bin/env bash

# Publish heading data
su - pi -c ~pi/git/FRC-2018/bin/heading-publisher.sh

su - pi -c ~pi/git/FRC-2018/bin/rope-tracker.sh
#su - pi -c ~pi/git/FRC-2018/bin/rope-publisher.sh

su - pi -c ~pi/git/FRC-2018/bin/msg-logger.sh

su - pi -c ~pi/git/FRC-2018/bin/system-metrics.sh

