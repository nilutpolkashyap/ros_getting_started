#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32, String

def callback(data, pub_odd_even):
    rospy.loginfo("Received: %d", data.data)

    # Check if the received number is odd or even
    if data.data % 2 == 0:
        result_str = "Even"
        pub_odd_even.publish(result_str)
        rospy.loginfo("Result: %s", result_str)
    else:
        result_str = "Odd"
        pub_odd_even.publish(result_str)
        rospy.loginfo("Result: %s", result_str)

def number_checker():
    rospy.init_node('number_checker', anonymous=True)
    # Publishers for even and odd strings
    pub_odd_even = rospy.Publisher("result", String, queue_size=10)

    # Subscriber to listen for integer
    rospy.Subscriber("my_topic", Int32, callback, pub_odd_even)

    rospy.spin()

if __name__ == '__main__':
    try:
        number_checker()
    except rospy.ROSInterruptException:
        pass
