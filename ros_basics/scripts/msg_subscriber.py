#!/usr/bin/env python 
import rospy 
from std_msgs.msg import String, Int32
from ros_basics.msg import greet

def callback(data):
	rospy.loginfo("Greetings : %s and Number : %d", data.greeting, data.number)

def listener():
	rospy.init_node("msg_subscriber", anonymous=True)
	rospy.Subscriber('greeting', greet, callback)

	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException():
		pass