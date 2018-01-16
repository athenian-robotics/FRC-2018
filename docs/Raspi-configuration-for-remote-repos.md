### FRC-2017 Repo

Setup a bare repo and a source directory:

```bash
$ cd ~/git
$ mkdir FRC-2017
$ mkdir FRC-2017.git
$ git init --bare ~/git/FRC-2017.git
```

Edit *FRC-2017.git/hooks/post-receive* and put this into it: 

```bash
#!/usr/bin/env sh
git --work-tree=/home/pi/git/FRC-2017 --git-dir=/home/pi/git/FRC-2017.git checkout -f
echo "*** Updated FRC-2017 ***" >&2
```

Make *post-receive* executable:
```bash
$ chmod +x ~/gitFRC-2017.git/hooks/post-receive
```
Adjust the git config on your Mac (change raspiXX to your raspi hostname):

```bash
$ cd ~/git/FRC-2017
$ git remote add raspiXX pi@raspiXX.local:/home/pi/git/FRC-2017.git
```

Push to the Raspi:
```bash
$ git push raspiXX master
```

### common-robotics Repo

Setup a bare repo and a source directory:

```bash
$ cd ~/git
$ mkdir common-robotics
$ mkdir common-robotics.git
$ git init --bare ~/git/common-robotics.git
```

Edit *common-robotics.git/hooks/post-receive* and put this into it: 

```bash
#!/usr/bin/env sh
git --work-tree=/home/pi/git/common-robotics --git-dir=/home/pi/git/common-robotics.git checkout -f
echo "*** Updated common-robotics.git ***" >&2
```

Make *post-receive* executable:
```bash
$ chmod +x ~/git/common-robotics.git/hooks/post-receive
```

Adjust the git config on your Mac (change raspiXX to your raspi hostname):

```bash
$ cd ~/git/common-robotics
$ git remote add raspiXX pi@raspiXX.local:/home/pi/git/common-robotics.git
```

Push to the Raspi:
```bash
$ cd ~/git/common-robotics
$ git push raspiXX master
```

### object-tracking Repo

Setup a bare repo and a source directory:

```bash
$ cd ~/git
$ mkdir object-tracking
$ mkdir object-tracking.git
$ git init --bare ~/git/object-tracking.git
```

Edit *object-tracking.git/hooks/post-receive* and put this into it: 

```bash
#!/usr/bin/env sh
git --work-tree=/home/pi/git/object-tracking --git-dir=/home/pi/git/object-tracking.git checkout -f
echo "*** Updated object-tracking.git ***" >&2
```

Make *post-receive* executable:
```bash
$ chmod +x ~/git/object-tracking.git/hooks/post-receive
```

Adjust the git config on your Mac (change raspiXX to your raspi hostname):

```bash
$ cd ~/git/object-tracking
$ git remote add raspiXX pi@raspiXX.local:/home/pi/git/object-tracking.git
```

Push to the Raspi:
```bash
$ cd ~/git/object-tracking
$ git push raspiXX master
```
