#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32

def publisher():
	rospy.init_node("float32_publisher", anonymous=True)
	pub = rospy.Publisher('float', Float32, queue_size=100)

	rate= rospy.Rate(10)
	var = 0.000

	while not rospy.is_shutdown():
		rospy.loginfo("Publisher sent : %f", var)
		pub.publish(var)
		rate.sleep()

		var = var + 0.05

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException():
		pass