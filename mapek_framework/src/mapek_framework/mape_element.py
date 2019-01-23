#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
import rospy
from .interaction import Interaction

class _MapeElement(object):

    __metaclass__ = ABCMeta

    input_interactions = []
    output_interactions = []

    def __init__(self, knowledge, managed_system):
        self.knowledge = knowledge
        self.managed_system = managed_system

        for interaction in self.input_interactions:
            rospy.Subscriber(interaction.name, interaction.data_class, 
                    lambda p: self.on_interaction_received(interaction.name, p))

        self.output_topics = {}
        for interaction in self.output_interactions:
            self.output_topics[interaction.name] = rospy.Publisher(interaction.name, interaction.data_class, queue_size=10)        

    @abstractmethod
    def on_interaction_received(self, interaction, payload):
        pass
    
    def send_interaction(self, interaction, payload):
        self.output_topics[interaction].publish(payload)


MonitorElement = _MapeElement
AnalyzeElement = _MapeElement
PlanElement = _MapeElement
ExecuteElement = _MapeElement
