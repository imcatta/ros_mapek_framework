#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from mapek_framework import Group, MapeElement, Interaction

class AnalyzeElement(MapeElement):

    input_interactions = [
        Interaction('light_status', String)
    ]
    output_interactions = [
        Interaction('master_analyze_plan', String)
    ]

    def on_message_received(self, interaction, message):
        light, status = message.data.split(' ')
        self.knowledge[int(light)] = status  
        self.send_message('master_analyze_plan', light)

class PlanElement(MapeElement):

    input_interactions = [
        Interaction('master_analyze_plan', String)
    ]
    output_interactions = [
        Interaction('switch_light', String)
    ]

    def on_message_received(self, interaction, message):
        light = int(message.data)
        if light % 2 == 0:
            self.send_message('switch_light', '%d on' % light)
        elif light != 0 and self.knowledge.get(light - 1, 'ko') == 'ko':
            self.send_message('switch_light', '%d on' % light)
        else:
            self.send_message('switch_light', '%d off' % light)


class MasterGroup(Group):
    elements = [AnalyzeElement, PlanElement]
    

def main():
    master = MasterGroup()
    rospy.init_node('master')
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
