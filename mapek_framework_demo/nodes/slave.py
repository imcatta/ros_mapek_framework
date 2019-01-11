#!/usr/bin/env python
import random
import sys
import rospy
from std_msgs.msg import String
from mapek_framework import Group, MapeElement, ManagedSystem, Interaction

class LightPoleMS(ManagedSystem):

    working = None

    def is_working(self):
        self.working = random.randint(0, 8) != 0
        return self.working

    def turn_on(self):
        if self.working:
            rospy.loginfo('ON')
        else:
            rospy.loginfo('BROKEN')

    def turn_off(self):       
        if self.working:
            rospy.loginfo('OFF')
        else:
            rospy.loginfo('BROKEN')

class MonitorElement(MapeElement):

    input_interactions = [
        Interaction('tick', String)
    ]
    output_interactions = [
        Interaction('light_status', String)
    ]

    def on_message_received(self, interaction, message):
        status = 'ok' if self.managed_system.is_working() else 'ko'
        self.send_message('light_status', '%s %s' % (self.knowledge['group_name'], status))

class ExecuteElement(MapeElement):

    input_interactions = [
        Interaction('switch_light', String)
    ]
    
    def on_message_received(self, interaction, message):
        light, status = message.data.split(' ')
        if light == str(self.knowledge['group_name']):
            if status == 'on':
                self.managed_system.turn_on()
            else:
                self.managed_system.turn_off()


class SlaveGroup(Group):
    elements = [MonitorElement, ExecuteElement]
    managed_system = LightPoleMS()

    def __init__(self, group_name):
        super(SlaveGroup, self).__init__()
        self.knowledge['group_name'] = group_name

def main():
    rospy.init_node('slave', anonymous=True)
    argv = rospy.myargv(argv=sys.argv)
    name = argv[1]
    slave = SlaveGroup(name)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
