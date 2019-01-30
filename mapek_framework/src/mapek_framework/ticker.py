#!/usr/bin/env python
"""
ticker.py
---------
"""
import rospy
from std_msgs.msg import Empty


class Ticker(object):
    """
    A simple object that publish 'tick' messages on a ROS topic at a given rate.

    Args:
        node_name (str): The desired ROS node name.
        topic (str): The topic on which to send the ticks.
        param3 (double): The rate of tick's pubblication.
    """

    def __init__(self, node_name, topic, rate):
        self._node_name = node_name
        self._topic = topic
        self._rate = rate

    def spin(self):
        """
        Start the ticker.
        """
        rospy.init_node(self._node_name)
        pub = rospy.Publisher(self._topic, Empty, queue_size=10)
        rate = rospy.Rate(self._rate)
        while not rospy.is_shutdown():
            pub.publish(Empty())
            rate.sleep()
