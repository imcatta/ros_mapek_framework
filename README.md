# ROS MAPE-K Framework

[![Build Status](https://travis-ci.org/imcatta/ros-mapek-framework.svg?branch=master)](https://travis-ci.org/imcatta/ros-mapek-framework)

### How to install
0. [Install ROS](http://wiki.ros.org/melodic/Installation). The full version is required. 
1. Set up a catkin workspace (see [this tutorials](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)). Make sure that the workspace path does not contains any special characters.
2. Clone this repository into the src/ folder. It should look like `/path/to/your/catkin_workspace/src/ros_mapek_framework`.
3. Activate your workspace 
```bash
cd /path/to/your/catkin_workspace
source devel/setup.bash
```
4. Build 
```bash
catkin_make
```

### Run the demo
1. Activate your workspace 
```bash
cd /path/to/your/catkin_workspace
source devel/setup.bash
```
2. Launch the demo using `roslaunch`
```bash
roslaunch mapek_framework_demo demo.launch
```
3. (Optional) Inspect nodes using `rqt_graph` and `rosrun rqt_console rqt_console`.
![Screenshot](docs/images/rqt_graph_screenshot.png)
![Screenshot](docs/images/rqt_console_screenshot.png)
