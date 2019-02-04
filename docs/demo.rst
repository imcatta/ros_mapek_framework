Demo
============

The demo aims to emulate a sequence of light poles
along a path. To save energy, the light poles are turned on
in an alternate fashion (in this specific case one on and one off, but it is possible to change criterion).
If, for some reasons, a light bulbs went out the system will be able to self-heal himself
by adjusting the list of lights on to reduce
at least the discomfort due to the breakage of the bulb.

Run the demo
------------

1. Activate your workspace.

.. code-block:: bash

  cd /path/to/your/catkin_workspace
  source devel/setup.bash

2. Launch the demo using `roslaunch`.

.. code-block:: bash

  roslaunch mapek_framework_demo demo.launch

3. (Optional) Inspect nodes using `rqt_graph` and `rosrun rqt_console rqt_console`.

.. image:: images/rqt_graph_screenshot.png
  :align: center
  
.. image:: images/rqt_console_screenshot.png
  :align: center
