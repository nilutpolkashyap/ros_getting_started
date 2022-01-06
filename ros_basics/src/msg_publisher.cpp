#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "ros_basics/greet.h"
#include <iostream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "msg_publisher");
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<ros_basics::greet>("/greeting",10);
	ros::Rate loop_rate(10);

	int num = 0;

	while(ros::ok())
	{
		ros_basics::greet msg;
		std::stringstream ss;
		ss << "Hello ROS user!" ;
		msg.greeting = ss.str();

		msg.number = num;

		ROS_INFO("Greeting: %s", msg.greeting.c_str());
		ROS_INFO("Number: %d", msg.number);
		pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
		++num;
	}
	return 0;
}