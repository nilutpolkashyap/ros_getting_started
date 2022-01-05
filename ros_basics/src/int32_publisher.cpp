#include "ros/ros.h"
#include "std_msgs/Int32.h"

#include <iostream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "int32_publisher");
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::Int32>("/integer",10);
	ros::Rate loop_rate(2);

	int count = 0;

	while(ros::ok())
	{
		std_msgs::Int32 msg;
		msg.data = count;
		ROS_INFO("Publisher sent: %d",msg.data);
		pub.publish(msg);

		ros::spinOnce();
		loop_rate.sleep();
		++count;
	}
	return 0;
}