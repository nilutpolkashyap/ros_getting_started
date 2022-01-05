#!/usr/bin/env python
import rospy 
from std_msgs.msg import String, Int32
from ros_basics.msg import greet

def publisher():
	rospy.init_node("msg_publisher", anonymous=True)
	pub = rospy.Publisher('greet', greet, queue_size=100)

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():