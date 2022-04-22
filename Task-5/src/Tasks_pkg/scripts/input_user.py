#!/usr/bin/env python3
# Execute as a python3 script
# Description: Set linear and angular values for the Turtle.
import rospy				# Needed to create a ROS node -Python client library
# Message type that Turtlesim accepts - usually via the topic cmd_vel
from geometry_msgs.msg import Twist

class ControlTurtlesim():

    def __init__(self):
        rospy.init_node('input_user', anonymous=False)
        # input_user is the name of the node sent to the master

		# Message to screen
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")

        # Keys CTRL + c will stop this script
        rospy.on_shutdown(self.shutdown)

	    # Since we want to move the turtle, this node will pubish a
        # Twist message on topic /turtle1/cmd_vel. lets do that below-

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        # Here we are creating a handle to publish messages to a topic using

	    # Turtlesim will receive our messages 10 times per second.
        rate = rospy.Rate(10);
 
        rospy.loginfo("Set rate 10Hz")
        # We may want the user to specify the rate rather than echo a fixed rate.

        # create an object of the class Twist.
        move_cmd = Twist()

	# Linear speed in x in units/second: positive values imply forward,
	# handle Errors 
        while True:
            l=input('Please Enter linear velocity between [2,6]: ')
            try:
                l = float(l)
            except ValueError:
                print ('Valid number, please')
                continue
            if 2 <= l <= 6:
                break
            else:   
                print ('Valid linear value, please: [2:6]')
        while True:
            v=input('PLease Enter angular between [1,3]: ')
            try:
                v = float(v)
            except ValueError:
                print ('Valid angular value, please')
                continue
            if 1 <= v <= 3:
                break
            else:   
                print ('Valid range of angular, please: [1:3]')
                
        # Modify this value to change the Turtle's speed
        move_cmd.linear.x = l
 	
	# Modify this value to cause rotation rad/s
        move_cmd.angular.z = v
        
	# Loop until you type CTRL+c
        while not rospy.is_shutdown():
	         # publish Twist values to the Turtlesim node /cmd_vel
             # handle.publish(message class instance)
            self.cmd_vel.publish(move_cmd)

	        # wait for 0.1 seconds (10 HZ) and publish again
            rate.sleep()


    def shutdown(self):
        # You can stop turtlesim_move by publishing an empty Twist message
        rospy.loginfo("Stopping the turtle")

        self.cmd_vel.publish(Twist())

        # Give it some time to stop
        rospy.sleep(1)

if __name__ == '__main__':
    # Try and Except.
    # If an error is encountered, a try block code execution is stopped and
    # transferred down to the except block.

    try:
        ControlTurtlesim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
