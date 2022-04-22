#!/usr/bin/env python3
import rospy

from std_msgs.msg import Int16

def talker():
    rospy.init_node('PubCount', anonymous=True)
    pub= rospy.Publisher('Counter', Int16,queue_size=10)

    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
    
        count += 1   
        rospy.loginfo (count)
        pub.publish(count)
        rate.sleep()
if __name__ == "__main__":
     try:
        talker()
     except rospy.ROSInterruptException:
        pass
