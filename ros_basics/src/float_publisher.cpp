#include "ros/ros.h"
#include "std_msgs/Float32.h"
#include <iostream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "float_publisher");
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<std_msgs::Float32>("/float",10);

	ros::Rate loop_rate(10);

	float var = 0.1;

	while(ros::ok())
	{
		std_msgs::Float32 msg;
		msg.data = var;
		ROS_INFO("Publisher sent: %f", msg.data);
		pub.publish(msg);

		ros::spinOnce();
		loop_rate.sleep();
		var = var + 0.2;
	}
	return 0;
}