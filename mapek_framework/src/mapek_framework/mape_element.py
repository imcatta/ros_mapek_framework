#!/usr/bin/env python
import rospy

class Interaction(object):

    def __init__(self, name, data_class):
        self.name = name
        self.data_class = data_class

class MapeElement(object):

    input_interactions = []
    output_interactions = []

    def __init__(self, knowledge, managed_system):
        self.knowledge = knowledge
        self.managed_system = managed_system

        for interaction in self.input_interactions:
            rospy.Subscriber(interaction.name, interaction.data_class, 
                    lambda m: self.on_message_received(interaction.name, m))

        self.output_topics = {}
        for interaction in self.output_interactions:
            self.output_topics[interaction.name] = rospy.Publisher(interaction.name, interaction.data_class, queue_size=10)
        

    def on_message_received(self, interaction, message):
        pass
    
    def send_message(self, interaction, message):
        self.output_topics[interaction].publish(message)