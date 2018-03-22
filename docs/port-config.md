**The ports that the FMS allows us to use are ports ```5800-5810```. More details can be found at** https://wpilib.screenstepslive.com/s/currentCS/m/troubleshooting/l/705152-fms-whitepaper

###Port Assignments
#####Ros
For ROS, we will be using ```Port 5800```. To change the port, the following changes must be made in the ```~/.bashrc``` file of every device connected to ROS
1) Change the value of the environment variable `ROS_MASTER_URI` from `[roscore-ip]:11311` to `[roscore-ip]:5800`
2) At the end of the ```~/.bashrc``` file, add the following line: `alias roscore='roscore -port 5800'`

#####gRPC: 
```Port 5801```

#####Video Streaming 
```Port 5802```