#!/usr/bin/env python
import rospy 
from std_msgs.msg import String, Int32
from ros_basics.msg import greet

def publisher():
	rospy.init_node("msg_publisher", anonymous=True)
	pub = rospy.Publisher('greeting', greet, queue_size=100)

	rate = rospy.Rate(10)
	var = 0

	while not rospy.is_shutdown():
		msg = greet()
		strg = "Hi there %s" % var
		msg.greeting = strg
		rospy.loginfo("Greetings sent : %s", strg)
		rospy.loginfo("Number sent : %d", var)
		msg.number = var
		var = var + 1
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException():
		pass