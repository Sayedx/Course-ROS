#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(msg):
    rospy.loginfo("I heard {}".format(msg.data))

def listener():
    rospy.init_node("SubCount", anonymous=True)
    rospy.Subscriber('Counter', Int16,callback)
    rospy.spin()

if __name__ == "__main__":
    listener()