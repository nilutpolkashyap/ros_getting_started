#include "ros/ros.h"
#include "std_msgs/Float32.h"
#include <iostream>

void callback(const std_msgs::Float32::ConstPtr& msg)
{
	ROS_INFO("Subscriber received: %f", msg->data);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "float_subscriber");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("/float",10,callback);

	ros::spin();

	return 0;
}