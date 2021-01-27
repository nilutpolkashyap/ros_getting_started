#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rospy.loginfo("I heard %s", data.data)

def subscriber():
	rospy.init_node("string_subscriber", anonymous=True)
	rospy.Subscriber("string", String, callback)

	rospy.spin()

if __name__ == '__main__':
	subscriber()
