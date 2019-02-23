#!/usr/bin/env python
"""
mape_components.py
---------------
"""
from abc import ABCMeta, abstractmethod
import rospy
from .interaction import Interaction


class _MapeComponent(object):
    """
    Abstract class that rappresents a generic mape component.

    Warning:
        This class or any subclasses of this class are not supposed to be instantiated explicitly.
        The :class:`~mapek_framework.group.Group` class will do that for you.
    """

    __metaclass__ = ABCMeta

    input_interactions = []
    """Component's input interactions."""

    output_interactions = []
    """Component's output interactions."""

    def __init__(self, knowledge, managed_system):
        self.knowledge = knowledge
        self.managed_system = managed_system

        for interaction in self.input_interactions:
            rospy.Subscriber(interaction.name, interaction.data_class,
                             lambda p: self.on_interaction_received(interaction.name, p))

        self.output_topics = {}
        for interaction in self.output_interactions:
            self.output_topics[interaction.name] = rospy.Publisher(
                interaction.name, interaction.data_class, queue_size=10)

    @abstractmethod
    def on_interaction_received(self, interaction, payload):
        """
        Override this method to implement the component logic.

        Warning:
            This method is not supposed to be called explicitly.
            The :class:`~mapek_framework.group.Group` class will do that for you.
        """

    def send_interaction(self, interaction, payload):
        """Send a message using an `output_interaction`."""
        self.output_topics[interaction].publish(payload)


class MonitorComponent(_MapeComponent):
    """Class that rappresents a Monitor component."""
    pass


class AnalyzeComponent(_MapeComponent):
    """Class that rappresents an Analyze component."""
    pass


class PlanComponent(_MapeComponent):
    """Class that rappresents a Plan component."""
    pass


class ExecuteComponent(_MapeComponent):
    """Class that rappresents an Execute component."""
    pass
