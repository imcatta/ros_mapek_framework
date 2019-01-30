#!/usr/bin/env python
"""
group.py
--------
"""
import rospy


class Group(object):
    """
    Class that rappresents a group of mape elements.

    Args:
        node_name (str): The desired ROS node name.
        **kwargs: Custom parameters to use to initialize the ROS node.
    """

    elements = []
    """Elements that are part of the group."""

    managed_system = None
    """The managed system that interacts with the group."""

    knowledge = {}
    """A dictionary-like object that rappresents the group knowledge."""

    def __init__(self, node_name, **kwargs):
        rospy.init_node(node_name, **kwargs)
        for element_class in self.elements:
            element_class(self.knowledge, self.managed_system)

    def spin(self):
        """
        Start the group.
        """
        rospy.spin()
