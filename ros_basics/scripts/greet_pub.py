import rospy 
from ros_basics.msg import greet

def greet_publisher():
    rospy.init_node("greet_publisher", anonymous=True)
    pub = rospy.Publisher("greeting", greet, queue_size=10)
    rate = rospy.Rate(2)

    var = 0
    
    while not rospy.is_shutdown():
        my_var = greet()
        my_var.greeting = "Hello"
        rospy.loginfo("Greetings sent: %s", my_var.greeting)

        my_var.number = var
        var = var + 1
        rospy.loginfo("Number sent: %d", my_var.number)

        pub.publish(my_var)

        rate.sleep()

if __name__ == '__main__':
    greet_publisher()

