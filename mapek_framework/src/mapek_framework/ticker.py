#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty

class Ticker(object):

    def __init__(self, node_name, topic, rate):
        self._node_name = node_name
        self._topic = topic 
        self._rate = rate

    def spin(self):
        rospy.init_node(self._node_name)
        pub = rospy.Publisher(self._topic, Empty, queue_size=10)
        rate = rospy.Rate(self._rate)
        while not rospy.is_shutdown():
            pub.publish(Empty())
            rate.sleep()