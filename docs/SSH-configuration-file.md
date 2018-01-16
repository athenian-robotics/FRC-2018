Create a *~/.ssh/config* file and set its permissions:

```bash
$ touch ~/.ssh/config
$ chmod 400 ~/.ssh/config
```

Add these entries to the file:

```
Host gear camera-gear camera-gear.local
  HostName camera-gear.local
  User pi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null

Host rope camera-rope camera-rope.local
  HostName camera-rope.local
  User pi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null

Host lidar lidar-gear lidar-gear.local
  HostName lidar-gear.local
  User pi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null

Host lcd1 lcd1.local
  HostName lidar-gear-left.local
  User pi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null

Host mqtt-turtle mqtt-turtle.local
  HostName mqtt-turtle.local
  User pi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null
```