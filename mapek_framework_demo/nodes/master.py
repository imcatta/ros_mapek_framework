#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from mapek_framework import Group, AnalyzeElement, PlanElement, Interaction

class MyAnalyzeElement(AnalyzeElement):

    input_interactions = [
        Interaction('light_status', String)
    ]
    output_interactions = [
        Interaction('master_analyze_plan', String)
    ]

    def on_interaction_received(self, interaction, payload):
        light, status = payload.data.split(' ')
        self.knowledge[int(light)] = status  
        self.send_interaction('master_analyze_plan', light)

class MyPlanElement(PlanElement):

    input_interactions = [
        Interaction('master_analyze_plan', String)
    ]
    output_interactions = [
        Interaction('switch_light', String)
    ]

    def on_interaction_received(self, interaction, payload):
        light = int(payload.data)
        if light % 2 == 0:
            self.send_interaction('switch_light', '%d on' % light)
        elif light != 0 and self.knowledge.get(light - 1, 'ko') == 'ko':
            self.send_interaction('switch_light', '%d on' % light)
        else:
            self.send_interaction('switch_light', '%d off' % light)


class MasterGroup(Group):
    elements = [MyAnalyzeElement, MyPlanElement]
    

def main():
    master = MasterGroup('master')
    master.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
