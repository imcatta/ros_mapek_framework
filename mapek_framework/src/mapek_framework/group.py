#!/usr/bin/env python

class Group(object):
    elements = []
    managed_system = None
    knowledge = {}

    def __init__(self):
        for element_class in self.elements:
            element_class(self.knowledge, self.managed_system)

