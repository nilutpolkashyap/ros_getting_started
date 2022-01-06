# ros_basics

# ROS Learning Resources

- ROS Basics  tutorials - http://wiki.ros.org/ROS/Tutorials
- package.xml file - http://wiki.ros.org/catkin/package.xml
- CMakeLists.txt file - http://wiki.ros.org/catkin/CMakeLists.txt
- ROS Bag files - http://wiki.ros.org/ROS/Tutorials/reading%20msgs%20from%20a%20bag%20file  
- catkin commands - http://wiki.ros.org/catkin/commands

# A collection of codes for ROS Basics 

## ROS Topics - Publisher & Subscriber 
1. **Integer** Publisher & Subscriber 
    - C++ Nodes - <br>
    ``` rosrun ros_basics int32_publisher ``` <br>
    ``` rosrun ros_basics int32_subscriber ```

    - Python Nodes - <br>
    ``` rosrun ros_basics int32_publisher.py ``` <br>
    ``` rosrun ros_basics int32_subscriber.py ```

    - Launch Files (C++ Nodes default) - <br>
    ``` roslaunch ros_basics int32_launch.launch```

<div align="center"> <img  alt="GUI" width="50%" src="https://raw.githubusercontent.com/nilutpolkashyap/ros_basics/main/images/integer_topic.png" /> <br /> </div>

2. **Float** Publisher & Subscriber 
    - C++ Nodes - <br>
    ``` rosrun ros_basics float_publisher ``` <br>
    ``` rosrun ros_basics float_subscriber ```

    - Python Nodes - <br>
    ``` rosrun ros_basics float_publisher.py ``` <br>
    ``` rosrun ros_basics float_subscriber.py ```

    - Launch Files (C++ Nodes default) - <br>
    ``` roslaunch ros_basics float_launch.launch```

<div align="center">
<img  alt="GUI" width="50%" src="https://raw.githubusercontent.com/nilutpolkashyap/ros_basics/main/images/float_topic.png" />
<br />
</div>

3. **String** Publisher & Subscriber
    - C++ Nodes - <br>
    ``` rosrun ros_basics string_publisher ``` <br>
    ``` rosrun ros_basics string_subscriber ```

    - Python Nodes - <br>
    ``` rosrun ros_basics string_publisher.py ``` <br>
    ``` rosrun ros_basics string_subscriber.py ```

    - Launch Files (C++ Nodes default) - <br>
    ``` roslaunch ros_basics string_launch.launch```

<div align="center">
<img  alt="GUI" width="50%" src="https://raw.githubusercontent.com/nilutpolkashyap/ros_basics/main/images/string_topic.png" />
<br />
</div>

-------------------------------------------------------------------

## Custom Message files - 'msg'
1. Custom 'greet.msg' file <br>
    ``` rosmsg show greet ``` <br>
    <div> <img  alt="GUI" width="25%" src="https://github.com/nilutpolkashyap/ros_basics/raw/main/images/greet_msg.JPG" /> <br /> </div>

2. 'greet' message Publisher & Subscriber 
    - C++ Nodes - <br>
    ``` rosrun ros_basics msg_publisher ``` <br>
    ``` rosrun ros_basics msg_subscriber ```

    - Python Nodes - <br>
    ``` rosrun ros_basics msg_publisher.py ``` <br>
    ``` rosrun ros_basics msg_subscriber.py ```

    - Launch Files (C++ Nodes default) - <br>
    ``` roslaunch ros_basics custom_msg_launch.launch```

<div align="center">
<img  alt="GUI" width="50%" src="https://github.com/nilutpolkashyap/ros_basics/raw/main/images/msg_launch.png" />
<br />
</div>


<!-- ## GUI 
To control **Arm** and **Gripper** of robot. <br/>
**GUI** Designed using **QT Designer** software.
<div align="center">
<img  alt="GUI" width="50%" src="https://raw.githubusercontent.com/nilutpolkashyap/gripper_bot/main/images/robot_gui.JPG" />
<br />
</div> -->
