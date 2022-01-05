#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "ros_basics/greet.h"
#include <iostream>

void callback(const ros_basics::greet::ConstPtr& msg)
{
	ROS_INFO("Received Message: %s", msg->greeting.c_str());
	ROS_INFO("Received Number: %d", msg->number);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "msg_subscriber");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("/greet",10,callback);

	ros::spin();
	return 0;
}