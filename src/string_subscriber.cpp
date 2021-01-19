#include "ros/ros.h"
#include "std_msgs/String.h"
#include <iostream>

void callback(const std_msgs::String::ConstPtr& msg)
{
	ROS_INFO("I received: %s", msg->data);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "string_subscriber");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("/string",10,callback);
	ros::spin();

	return 0;
}