#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo("This node has been started")
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        #Try to keep the rate at 10 Hz
        rate.sleep()
    
