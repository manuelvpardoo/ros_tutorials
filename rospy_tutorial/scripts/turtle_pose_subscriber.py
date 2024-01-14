#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def pose_callback(data):
    rospy.loginfo("Turtle Position: x=%.2f, y=%.2f, theta=%.2f", data.x, data.y, data.theta)

if __name__ == "__main__":
    rospy.init_node("turtle_pose_subscriber")
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rospy.spin()
