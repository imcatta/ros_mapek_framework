#!/usr/bin/env python
import rospy

class Group(object):
    elements = []
    managed_system = None
    knowledge = {}

    def __init__(self, node_name, **kwargs):
        rospy.init_node(node_name, **kwargs)
        for element_class in self.elements:
            element_class(self.knowledge, self.managed_system)

    def spin(self):
        rospy.spin()
