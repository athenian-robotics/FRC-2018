#!/bin/bash
# Usage: `. init_bare_repo.sh <repo_name>`
FILENAME=$1
cd /home/pi/git
mkdir -p /home/pi/git/$1.git
mkdir -p /home/pi/catkin_ws/src/$1
echo "#!/usr/bin/env sh
git --work-tree=/home/pi/catkin_ws/src/$1 --git-dir=/home/pi/git/$1.git checkout -f
echo \"*** Updated $1 ***\" >&2" >> /home/pi/git/$1.git/hooks/post_receive
chmod +x /home/pi/git/$1.git/hooks/post_receive
