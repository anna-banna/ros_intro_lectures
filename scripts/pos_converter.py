#!/usr/bin/env python3

import rospy 
from turtlesim.msg import Pose 
import math

ROTATION_SCALE = 180.0/math.pi 

def pose_callback(data): 
	rot_in_degree = data.theta * ROTATION_SCALE
	x_in_cm = data.x * 100 
	y_in_cm = data.y * 100
	rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degree) 
	
if __name__ == '__main__': 
	rospy.init_node('pos_converter', anonymous = True) 
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	rospy.spin()
