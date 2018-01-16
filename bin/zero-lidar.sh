#!/usr/bin/env bash

date > ~pi/git/FRC-2017/logs/zero-lidar.reboot
export PYTHONWARNINGS="ignore"
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics
export GOPATH=~pi/go
export GOBIN=~pi/go/bin
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
export PATH=/usr/local/go/bin:$PATH

python ~pi/git/distance-tracking/distance_server.py --did 00FEBABC --baud 115200 &> ~pi/git/FRC-2017/logs/distance_server.out &

go run ~pi/git/distance-tracking/http_proxy.go -stderrthreshold=INFO -logtostderr=true &> ~pi/git/FRC-2017/logs/http_proxy.out &
