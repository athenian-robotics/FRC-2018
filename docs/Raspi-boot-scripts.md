* Shell scripts are launched via a startup script in */etc/rc.local* during startup.
The startup script calls are added just before the call to `exit 0` and are executed as user *pi*:
````bash
~pi/git/FRC-2018/boot/camera-gear-startup.sh

exit 0
````

* The startup scripts are found in *~pi/git/FRC-2018/boot*

* The shell scripts are found in *~pi/git/FRC-2018/bin*

* All changes to scripts should be pushed to github and not done as a one-off 
edit on a Raspi. The goal is to provision a Raspi with `git` and minimize the amount 
of configuration on the Raspi. 

* Shell script stdout and stderr are redirected to *~pi/git/FRC-2018/logs*

* Shell scripts running Python code using OpenCV need to first setup a *cv2* environment with:
```bash
source ~pi/.profile
workon py2cv3
```

* Create a timestamp for the boot time with:
```bash
date > ~pi/git/FRC-2018/logs/object-tracker.reboot
```

* The *stdout* and *stderr* are included in the log file by using `&>`. It is critical that each shell script
be forked with a trailing `&`:
```bash
python2 ~pi/git/object-tracking/object_tracker.py --bgr "174, 56, 5" --width 400 --flip &> ~pi/git/FRC-2018/logs/object-tracker.out &
```

* The complete launch script would look like: 
```bash
#!/usr/bin/env bash
source ~pi/.profile
workon py2cv3
date > ~pi/git/FRC-2018/logs/object-tracker.reboot
python2 ~pi/git/object-tracking/single_object_tracker.py --bgr "174, 56, 5" --width 400 --delay 0.25 --flipy --usb --http "camera-gear.local:8080" &> ~pi/git/FRC-2018/logs/object-tracker.out &
```