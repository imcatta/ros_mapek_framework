How to install
==============

0. `Install ROS`_. The full version is required.

.. _`Install ROS`: http://wiki.ros.org/melodic/Installation

1. Set up a catkin workspace (see `this tutorial`_). Make sure that the workspace path does not contains any special characters.

.. _`this tutorial`: http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. Clone this repository into the src/ folder. It should look like `/path/to/your/catkin_workspace/src/ros_mapek_framework`.

3. Activate your workspace.

.. code-block:: bash

  cd /path/to/your/catkin_workspace
  source devel/setup.bash

4. Build.

.. code-block:: bash

 catkin_make
