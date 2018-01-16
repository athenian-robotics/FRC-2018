#!/usr/bin/env bash

# Reboot Robot Raspis
echo "Shutting Down Robot Raspis"
ssh -o StrictHostKeyChecking=no pi@mqtt-turtle.local sudo shutdown now
ssh -o StrictHostKeyChecking=no pi@camera-rope.local sudo shutdown now
ssh -o StrictHostKeyChecking=no pi@camera-gear.local sudo shutdown now
ssh -o StrictHostKeyChecking=no pi@lidar-gear.local sudo shutdown now
ssh -o StrictHostKeyChecking=no pi@lcd1.local sudo shutdown now
