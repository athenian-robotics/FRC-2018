### FRC-2018 Repo

Setup a bare repo and a source directory:

```bash
$ cd ~/git
$ mkdir FRC-2018
$ mkdir FRC-2018.git
$ git init --bare ~/git/FRC-2018.git
```

Edit *FRC-2018.git/hooks/post-receive* and put this into it: 

```bash
#!/usr/bin/env sh
git --work-tree=/home/pi/git/FRC-2018 --git-dir=/home/pi/git/FRC-2018.git checkout -f
echo "*** Updated FRC-2018 ***" >&2
```
**Warning** Use the absolute pathnames here.

Make *post-receive* executable:
```bash
$ chmod +x ~/gitFRC-2018.git/hooks/post-receive
```
Adjust the git config on your Mac (change raspiXX to your raspi hostname):

```bash
$ cd ~/git/FRC-2018
$ git remote add raspiXX pi@raspiXX.local:/home/pi/git/FRC-2018.git
```

Push to the Raspi:
```bash
$ git push raspiXX master
```
### Nvidia Vision Repo

Setup a bare repo and a source directory:

```bash
$ cd ~/git
$ mkdir 2018-Vision
$ mkdir 2018-Vision.git
$ git init --bare ~/git/2018-Vision.git
```

Edit *2018-Vision.git/hooks/post-receive* and put this into it: 

```bash
#!/usr/bin/env sh
git --work-tree=/home/nvidia/git/2018-Vision --git-dir=/home/nvidia/git/2018-Vision.git checkout -f
echo "*** Updated FRC-2018 ***" >&2
```
**Warning** Use the absolute pathnames here.

Make *post-receive* executable:
```bash
$ chmod +x ~/git2018-Vision.git/hooks/post-receive
```
Adjust the git config on your Mac (change Nvidia to your Nvidia hostname):

```bash
$ cd ~/git/2018-Vision
$ git remote add tegra nvidia@tegra-ubuntu.local:/home/nvidia/git/FRC-2018.git
```

Push to the Nvidia:
```bash
$ git push Nvidia master
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
