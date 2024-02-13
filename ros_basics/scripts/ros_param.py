import rospy

def ros_parameter_example():
    rospy.init_node("ros_param_node")

    frequency = 1.6
    rospy.set_param('frequency', frequency)
    rospy.loginfo("New frequency: %s hz", frequency)

    robot_value = rospy.get_param('/robot1/param1', default=0.001)
    rospy.loginfo("Value: %f", robot_value)

    param_list = rospy.get_param_names()
    rospy.loginfo("all active parameters: %s", param_list)

    if rospy.has_param('/robot3/param1'):
        value = rospy.get_param('/robot3/param1')
        rospy.loginfo("Robot 3 value: %s", value)
    else:
        rospy.logwarn("Parameter '/robot3/param1' not found")
        rospy.logerr("Parameter '/robot3/param1' not found")

    while True:
        robot_radius = rospy.get_param("/robot1/robot_radius", default=0.01)
        rospy.loginfo("Robot radius : %s", robot_radius)

if __name__ == '__main__':
    try:
        ros_parameter_example()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass