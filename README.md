# SAYABOT #

This packages were developed and tested in __ROS Indigo__ Distro. This packages also supports __ROS Jade__. 

This repository is for sayabot hospitality robot.
This contains ros-packages for the same.



## Sayabot Hospitality ##

* Ros Packages



## List of Ros Packages ##

* saya_hospitality_perception
* saya_hospitality_navigation
* saya_hospitality_manipulation
* saya_hospitality_scenarios
* saya_hospitality_communication



## Package Installation ##

-----------------------

### Install Ros ###

Install Ros in your system from this [link](http://wiki.ros.org/indigo/Installation/Ubuntu)

-----------------------

### Create Workspace ###

Create workspace in your HOME directory:

	$ mkdir -p ~/sayabot_ws/src
	$ cd ~/sayabot_ws/src
	$ catkin_init_workspace

Then, Build your workspace

	$ cd ~/sayabot_ws/
	$ catkin_make

Now source your new setup.*sh file:

	$ source devel/setup.bash

For further assit in creating workspace, click [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

-----------------------

### Clone the Git Repository ###

Install the sound-play package

sudo apt-get install ros-indigo-sound-play

Follow the code to clone this repository.

	$ cd ~/sayabot_ws/src
	$ git clone https://github.com/gokul-gokz/IRA_v1.git # (copy the url from clone option in bitbucket)

-----------------------

### Build Workspace ###

	$ cd ~/sayabot_ws/
	$ catkin_make

-----------------------

### NOTE ###

1.Read the README file in each package before running it.

2.Other package to download inside the workspace.
	a)navigation-indigo-devel
	b)robot_pose_publisher-develop
	c)rosserial
	d)learning_tf
