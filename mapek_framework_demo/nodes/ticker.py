#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def main():
    pub = rospy.Publisher('tick', String, queue_size=10)
    rospy.init_node('ticker')
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        pub.publish('tick')
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
