#!/usr/bin/env python

import rospy
from std_msgs.msg import String 

def talker():
	rospy.init_node('simple_py_publisher', anonymous=True)
	pub = rospy.Publisher('chatter', String, queue_size=10)

	rate = rospy.Rate(10)
	count = 0

	while not rospy.is_shutdown():
		str1 = "hello world %s " % count
		rospy.loginfo(str1)
		pub.publish(str1)

		rate.sleep()

		count = count + 1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass