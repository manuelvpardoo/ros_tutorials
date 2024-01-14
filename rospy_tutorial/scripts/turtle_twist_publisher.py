#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("turtle_twist_publisher")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 1.0  # Adjust the linear velocity as needed
        twist_msg.angular.z = 0.5  # Adjust the angular velocity as needed
        pub.publish(twist_msg)
        rate.sleep()
