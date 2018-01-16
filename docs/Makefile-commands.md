The following Makefile commands are available:

| Command            | Description                      |
|:-------------------|:---------------------------------|
|`make github-push`  | Pushes to *common-robotics*, *FRC-2018*, *FRC-2018-robot* and *object-tracking* repos on github (must be connected to *TASGUEST*)|
|`make github-pull`  | Pulls from *common-robotics*, *FRC-2018*, *FRC-2018-robot* and *object-tracking* repos on github (must be connected to *TASGUEST*)|
|`make robot`        | Pushes to the Raspis on the robot (must be connected to *852*) |
|`make reboot`       | Reboots the Raspis on the robot (must be connected to *852*) |
|`make shutdown`     | Shuts down the Raspis on the robot (must be connected to *852*) |
|`make clear-pyc`    | Removes python cache files from python repos |

Makefile commands can be combined, e.g., `make robot reboot`.