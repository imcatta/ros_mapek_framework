#!/usr/bin/env python
import random
import sys
import rospy
from std_msgs.msg import Empty, String
from mapek_framework import Group, MonitorElement, ExecuteElement, ManagedSystem, Interaction

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

class MyMonitorElement(MonitorElement):

    input_interactions = [
        Interaction('tick', Empty)
    ]
    output_interactions = [
        Interaction('light_status', String)
    ]

    def on_interaction_received(self, interaction, payload):
        status = 'ok' if self.managed_system.is_working() else 'ko'
        self.send_interaction('light_status', '%s %s' % (self.knowledge['group_name'], status))

class MyExecuteElement(ExecuteElement):

    input_interactions = [
        Interaction('switch_light', String)
    ]
    
    def on_interaction_received(self, interaction, payload):
        light, status = payload.data.split(' ')
        if light == str(self.knowledge['group_name']):
            if status == 'on':
                self.managed_system.turn_on()
            else:
                self.managed_system.turn_off()


class SlaveGroup(Group):
    elements = [MyMonitorElement, MyExecuteElement]
    managed_system = LightPoleMS()

    def __init__(self, group_name, node_name, **kwargs):
        super(SlaveGroup, self).__init__(node_name, **kwargs)
        self.knowledge['group_name'] = group_name

def main():
    name = rospy.myargv(argv=sys.argv)[1]
    slave = SlaveGroup(name, 'slave', anonymous=True)
    slave.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
