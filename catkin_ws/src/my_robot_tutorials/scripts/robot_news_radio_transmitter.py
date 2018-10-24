#!/ust/bin/env python

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('robot_news_radio_transmitter')

    #publish messages on some topics
    #topic name and message type as parameters
    #messages = std_msgs --> String
    #Then a queue size as a buffer
    pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

    #Publish data

    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        msg = String() #create a message
        msg.data = "Hi, this is the speaker of the Robot nws Radio!"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node was stopped!")


    
