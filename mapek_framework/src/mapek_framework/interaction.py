#!/usr/bin/env python
"""
interaction.py
--------------
"""

class Interaction(object):
    """
    Class that rappresents an interaction between instances of mape elements.

    Args:
        name (str): Name of the interaction.
        data_class: ROS message type associated with the interaction.
    """

    def __init__(self, name, data_class):
        self.name = name
        self.data_class = data_class
