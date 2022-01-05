#include "ros/ros.h"
#include "std_msgs/String.h"

#include <iostream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "string_publisher");
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::String>("/string",10);
	ros::Rate loop_rate(10);

	while(ros::ok())
	{
		std_msgs::String msg;
		msg.data = "Hello World";
		ROS_INFO("Publisher sent: %s", msg.data.c_str());
		pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();

	}
	return 0;

}