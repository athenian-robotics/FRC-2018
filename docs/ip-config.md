
# IP Address Config
## IP Addresses per Device
For info on the addresses we're allowed to use, visit https://wpilib.screenstepslive.com/s/currentCS/m/troubleshooting/l/319135-ip-networking-at-the-event
All devices have a subnet of ```255.255.255.0``` unless otherwise stated
### RoboRio
```10.8.52.2```
### Driver Station
```10.8.52.5```
Subnet: ```255.0.0.0```
### Jetson
```10.8.52.8```
### rospiled
```10.8.52.9```
### roscore
```10.8.52.10```
### rospi1
```10.8.52.11```
### rospi2
```10.8.52.12```
## How to Assign IP Addresses
This is how the file ```/etc/network/interfaces``` should look:
```angular2html
source-directory /etc/network/interfaces.d


auto lo
iface lo inet loopback


allow-hotplug enx*
iface enx* inet static #Replace enx* with what shows up in ifconfig
address  10.8.52.* #Replace * with correct number 
netmask 255.255.255.0
gateway 10.8.52.1

```

After making the changes, run `sudo ifdown enx*` and `sudo ifup enx*`.



