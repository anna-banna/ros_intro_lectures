#!/usr/bin/env python3

import rospy 
from turtlesim.msg import Pose 
#import the new message 
from ros_intro_lectures.msg import Shortpose
import math

ROTATION_SCALE = 180.0/math.pi 

#defining a global variable
#has x, y, and theta
pos_msg = Shortpose()

def pose_callback(data): 
	global pos_msg
	pos_msg.theta = data.theta * ROTATION_SCALE
	pos_msg.x = data.x * 100 
	pos_msg.y = data.y * 100
	#rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degree) 
	
	
if __name__ == '__main__': 
	rospy.init_node('pos_publisher', anonymous = True) 
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	pose_pub = rospy.Publisher('turtle1/short_pose', Shortpose, queue_size = 10)

	#set the frequency at 10Hz
	loop_rate = rospy.Rate(10)

	#set up control loop
	while not rospy.is_shutdown(): 
	
		
		
		#publish the message
		pose_pub.publish(pos_msg)
		
		#sleep for some time until the next iteration
		loop_rate.sleep()
