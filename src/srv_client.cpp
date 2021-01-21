#include "ros/ros.h"
#include "ros_basics/serve.h"
#include <iostream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "srv_client");
	ros::NodeHandle nh;
	ros::Rate loop_rate(10);
	ros::ServiceClient client = nh.serviceClient<ros_basics::serve>("service");

	while(ros::ok())
	{
		ros_basics::serve srv;
		std::stringstream ss;
		ss << "Sending: ";
		srv.request.in = ss.str();

		if(client.call(srv))
		{
			ROS_INFO("From client %s, Server says %s", srv.request.in.c_str(), srv.response.out.c_str());
		}
		else
		{
			ROS_ERROR("FAILED");
			return 1;
		}
		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}