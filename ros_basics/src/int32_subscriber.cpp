#include "ros/ros.h"
#include "std_msgs/Int32.h"

#include <iostream>

void callback(const std_msgs::Int32::ConstPtr& msg)
{
	ROS_INFO("Subscriber received: %d", msg->data);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "int32_subscriber");
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("/integer",10,callback);

	ros::spin();

	return 0;
}