[![Code Health](https://landscape.io/github/athenian-robotics/FRC-2017/master/landscape.svg?style=flat)](https://landscape.io/github/athenian-robotics/FRC-2017/master)
[![Code Climate](https://codeclimate.com/github/athenian-robotics/FRC-2017/badges/gpa.svg)](https://codeclimate.com/github/athenian-robotics/FRC-2017)

# FRC-2017 Notes

## RoboRio

The RoboRio hostname is *roborio-852-frc.local*.  The configuration page is at: *http://roborio-852-frc.local*

## Raspi Names

| #   | Name                       |Static IP Address  | Repos                                              |
|:---:|:---------------------------|:------------------|:---------------------------------------------------|
| 11  | **camera-gear.local**      |10.8.52.103        | [common-robotics](https://github.com/athenian-robotics/common-robotics), [FRC-2017](https://github.com/athenian-robotics/FRC-2017), [object-tracker](https://github.com/athenian-robotics/object-tracking)          |
| 18  | **camera-rope.local**      |10.8.52.104        | [common-robotics](https://github.com/athenian-robotics/common-robotics), [FRC-2017](https://github.com/athenian-robotics/FRC-2017), [object-tracker](https://github.com/athenian-robotics/object-tracking)          |
| 10  | **lidar-gear.local**       |10.8.52.105        | [common-robotics](https://github.com/athenian-robotics/common-robotics), [FRC-2017](https://github.com/athenian-robotics/FRC-2017)                          |
| 24  | **lcd1.local**             |10.8.52.100        | [common-robotics](https://github.com/athenian-robotics/common-robotics), [FRC-2017](https://github.com/athenian-robotics/FRC-2017) |
| 12  | **mqtt-turtle.local**      |10.8.52.102        | none                                               |

## MQTT Topics 
| Name                             | Description                                             |
|:---------------------------------|:--------------------------------------------------------|
|**camera/gear/x**                 | Camera center position and screen width (String:String) |
|**camera/gear/peg/x**             | Peg position and screen width (String:String)           |
|**camera/gear/dualtape/x**        | Avg dual tape position and screen width (String:String) |
|**camera/gear/alignment**         | Camera relative to object (String)                      |
|**lidar/left/mm**                 | Left lidar distance (String)                            |
|**lidar/right/mm**                | Right lidar distance (String)                           |
|**lidar/front/cm**                | Front lidar distance (String)                           |
|**lidar/rear/cm**                 | Rear lidar distance (String)                            |
|**heading/degrees**               | Heading degrees (String)                                |
|**heading/calibration**           | Calibration status (String)                             |
|**metrics/msg_rate**              | Msgs/Sec (String)                                       |
|**logging/camera/gear/alignment** | Logging info (String)                                   |
|**logging/lidar/gear/distance**   | Logging info (String)                                   |
|**logging/heading/degrees**       | Logging info (String)                                   |
|**logging/metrics/msg_rate**      | Logging info (String)                                   |

## Arduino Device IDs
| Location                  | ID                                                      |
|:--------------------------|:--------------------------------------------------------|
|Heading (Arduino)          | 95530343235351A0E0A2                                    |
|Heading (Metro)            | 00FEBA85                                                |
|Left lidar                 | 7543331373935160E190                                    |
|Right lidar                | 95538333535351019130                                    |
|Front lidar                | 00FEBA8B                                                |
|Rear lidar                 | 00FEBA73                                                |


## Heading Sensor

The heading sensor calibration is described [here](https://learn.adafruit.com/bno055-absolute-orientation-sensor-with-raspberry-pi-and-beaglebone-black/webgl-example?embeds=allow#sensor-calibration)

## Metro Mini SNs

Metro Minis do not report their SN via the Arduin IDE. Use:
```bash
$ cd git/common-robotcs
$ ./metro_minis.py
```
 
## SSH Setup

* [SSH Configuration](https://github.com/athenian-robotics/FRC-2017/wiki/SSH-configuration-file)
* [Using SSH without a password](https://github.com/athenian-robotics/FRC-2017/wiki/Using-SSH-without-a-password)


## Remote repo setup for Raspis

Setting up remote repos on Raspis will allow you to push changes to Raspis without the Raspis
have access to github.

* [OSX Configuration](https://github.com/athenian-robotics/FRC-2017/wiki/OSX-configuration-for-remote-repos)
* [Raspi Configuration](https://github.com/athenian-robotics/FRC-2017/wiki/Raspi-configuration-for-remote-repos)


## Raspi launch scripts

* [Makefile commands](https://github.com/athenian-robotics/FRC-2017/wiki/Makefile-commands)
* [Raspi boot scripts](https://github.com/athenian-robotics/FRC-2017/wiki/Raspi-boot-scripts)

## Camera Image Requirements

* Repos: [common-robotics](https://github.com/athenian-robotics/common-robotics), [FRC-2017](https://github.com/athenian-robotics/FRC-2017), [object-tracker](https://github.com/athenian-robotics/object-tracking)  

### PIP requirements

Raspbian with the *pysearchimages* distro (has OpenCV 3.2 package):

```bash
$ source start_py2cv3.sh
$
$ pip install --upgrade setuptools pip
$ pip install -r pip/requirements.txt
$ pip install -r pip/opencv-requirements.txt
$
$ pip3 install --upgrade setuptools pip
$ pip3 install -r pip/requirements.txt
$ pip3 install -r pip/opencv-requirements.txt
```

Vanilla Raspbian:

```bash
$ sudo pip install --upgrade setuptools pip
$ sudo pip install -r pip/requirements.txt
$
$ sudo pip3 install --upgrade setuptools pip
$ sudo pip3 install -r pip/requirements.txt
```

### apt-get requirements
```bash
$ sudo apt-get install git
$ sudo apt-get install python
$ sudo apt-get install python-dev
$ sudo apt-get install python-blinkt
$ sudo apt-get install nginx
```

## /etc/rc.local scripts

These snipets are appended above `exit 0` statement:

lidar-gear:

```bash
~pi/git/FRC-2017/boot/lidar-gear-startup.sh
```
camera-gear:
  
```bash
~pi/git/FRC-2017/boot/camera-gear-startup.sh
```

camera-rope:
  
```bash
~pi/git/FRC-2017/boot/camera-rope-startup.sh
```

lcd1:

```bash
~pi/git/FRC-2017/boot/lcd1-startup.sh
```

## /etc/ssh/sshd_config edits for turning off reverse DNS lookup

Details are [here](https://linux-tips.com/t/disabling-reverse-dns-lookups-in-ssh/222)

Add this line to the bottom of */etc/ssh/sshd_config*:
```
UseDNS no
```

Restart sshd with: 
```bash
$ service ssh reload
```

## /etc/dhcpcd.conf edits for Raspi static IP addresses 

Details are [here](https://www.modmypi.com/blog/how-to-give-your-raspberry-pi-a-static-ip-address-update).

### lidar-gear.local

```
interface eth0
static ip_address=10.8.52.105/24
static routers=10.8.52.1
static domain_name_servers=10.8.52.1
```

### camera-gear.local

```
interface eth0
static ip_address=10.8.52.103/24
static routers=10.8.52.1
static domain_name_servers=10.8.52.1
```

### camera-rope.local

```
interface eth0
static ip_address=10.8.52.104/24
static routers=10.8.52.1
static domain_name_servers=10.8.52.1
```


### mqtt-turtle.local

```
interface eth0
static ip_address=10.8.52.102/24
static routers=10.8.52.1
static domain_name_servers=10.8.52.1
```

### lcd1.local

```
interface eth0
static ip_address=10.8.52.100/24
static routers=10.8.52.1
static domain_name_servers=10.8.52.1
```

## Connecting to robot Raspis

When connecting to the robot Raspis, manually set your IP address to `10.8.52.201` and netmask to `255.0.0.0`.