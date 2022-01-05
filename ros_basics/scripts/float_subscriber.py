#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32

def callback(data):
	rospy.loginfo("Subscriber heard : %f", data.data)

def subscriber():
	rospy.init_node('float_subscriber', anonymous=True)
	rospy.Subscriber("float", Float32, callback)

	rospy.spin()

if __name__ == '__main__':
	try:
		subscriber()
	except rospy.ROSInterruptException():
		pass