#!/usr/bin/env python3

#import the ROS libraries into this node 
import rospy 

#import the geometry message, TWIST, from ROS libraries 
from geometry_msgs.msg import Twist 


if __name__ == '__main__':

	#define a publisher here for sending velocity commands 
	cmd_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)
	
	#initialize the node 
	rospy.init_node('vel_publisher_node', anonymous = True)
	
	#create a loop rate (timer)
	#set the frequency at 10Hz
	loop_rate = rospy.Rate(10)
	
	#create a message for sending the commands
	vel_cmd = Twist()
	
	#set up control loop
	while not rospy.is_shutdown(): 
	
		#prints hi every second (when rospy.Rate(1))
		#print('hi')
		
		#set the linear velocity 
		vel_cmd.linear.x = 1.0
		#set the angular velocity 
		vel_cmd.angular.z = 0.5
		
		#publish the message
		cmd_pub.publish(vel_cmd)
		
		#sleep for some time until the next iteration
		loop_rate.sleep()
		
		
		
		
		
		
	
	
	
	
	
