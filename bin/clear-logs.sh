#!/usr/bin/env bash

# Clearing Robot Raspi Logs
echo "Clearing Robot Raspi Logs and .pyc Files"
ssh -o StrictHostKeyChecking=no pi@camera-gear.local 'cd ~/git/FRC-2018; make _reset-logs _reset-pyc'
ssh -o StrictHostKeyChecking=no pi@camera-rope.local 'cd ~/git/FRC-2018; make _reset-logs _reset-pyc'
ssh -o StrictHostKeyChecking=no pi@lidar-gear.local 'cd ~/git/FRC-2018; make _reset-logs _reset-pyc'
ssh -o StrictHostKeyChecking=no pi@lcd1.local 'cd ~/git/FRC-2018; make _reset-logs _reset-pyc'
