default: help

help:
	echo "Try make github, make robot or make reboot"

robot:
	./bin/push-to-robot.sh

github-pull:
	./bin/pull-from-github.sh

github-push:
	./bin/push-to-github.sh

reboot:
	./bin/reboot-robot.sh

shutdown:
	./bin/shutdown-robot.sh

clear-logs:
	./bin/clear-logs.sh

_reset-pyc:
	rm -f ~/git/FRC-2018/*.pyc
	rm -f ~/git/object-tracking/*.pyc
	rm -f ~/git/common-robotics/*.pyc

_reset-logs:
	rm -f ~/git/FRC-2018/logs/*.out
	rm -f ~/git/FRC-2018/logs/*.reboot
	rm -f ~/git/FRC-2018/logs/*.log

camera-gear-logs:
	echo "********** Camera Gear Last Reboot Time **********"
	ssh camera-gear last reboot | head -1
	echo "********** Camera Gear Object Tracker **********"
	ssh camera-gear cat /home/pi/git/FRC-2018/logs/dual-tape-tracker.out
	echo "********** Camera Gear Publisher **********"
	ssh camera-gear cat /home/pi/git/FRC-2018/logs/gear-publisher.out

camera-rope-logs:
	echo "********** Camera Rope Last Reboot Time **********"
	ssh camera-rope last reboot | head -1
	echo "********** Camera Rope Object Tracker **********"
	ssh camera-rope cat /home/pi/git/FRC-2018/logs/rope-tracker.out
	echo "********** Camera Rope Publisher **********"
	ssh camera-rope cat /home/pi/git/FRC-2018/logs/rope-publisher.out

lidar-logs:
	echo "********** Lidar Gear Last Reboot Time **********"
	ssh lidar-gear last reboot | head -1
	echo "********** Left Lidar Publisher **********"
	ssh lidar-gear cat /home/pi/git/FRC-2018/logs/lidar-left-publisher.out
	echo "********** Right Lidar Publisher **********"
	ssh lidar-gear cat /home/pi/git/FRC-2018/logs/lidar-right-publisher.out
	echo "********** Heading Publisher **********"
	ssh lidar-gear cat /home/pi/git/FRC-2018/logs/heading_publisher.out

lcd1-logs:
	echo "********** LCD1 Last Reboot Time **********"
	ssh lcd1 last reboot | head -1
	echo "********** Left Lidar Publisher **********"
	ssh lcd1 cat /home/pi/git/FRC-2018/logs/lidar_display.out.out
