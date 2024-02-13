import rospy 
from std_msgs.msg import Int32, Float32, String
import random

def publisher():
    rospy.init_node("int32_publisher", anonymous=True)
    pub = rospy.Publisher("user_input_topic", Int32, queue_size=10)

    # rate = rospy.Rate(0.1)
    
    while not rospy.is_shutdown():
        var = int(input("Enter a number: "))
        rospy.loginfo("Publisher sent: %d", var)
        pub.publish(var)
        # rate.sleep()

if __name__ == '__main__':
    publisher()

