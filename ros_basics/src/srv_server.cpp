#include "ros/ros.h"
#include "ros_basics/serve.h"
#include <iostream>

bool callback(ros_basics::serve::Request &req, ros_basics::serve::Response &res)
{
	std::stringstream ss;
	ss << "Received: ";
	res.out = ss.str();
	ROS_INFO("From client: %s, Server says: %s", req.in.c_str(), res.out.c_str());
	return true;
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "srv_server");
	ros::NodeHandle nh;
	ros::ServiceServer server = nh.advertiseService("service", callback);
	ROS_INFO("Ready to recieve from client: ");
	ros::spin();

	return 0;
}