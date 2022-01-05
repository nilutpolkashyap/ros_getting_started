#!/usr/bin/env python
import rospy 
from std_msgs.msg import String

def publisher():
	pub = rospy.Publisher("string", String, queue_size = 10)
	rospy.init_node("string_publisher", anonymous=True)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		str = "hello from Publisher" 
		rospy.loginfo("Publisher sent : %s", str)
		pub.publish(str)
		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass