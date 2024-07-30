#!/usr/bin/env python

import rospy
from geometry_msgs.msg import TransformStamped, PoseStamped

def transform_to_pose(transform):
    pose = PoseStamped()
    pose.header = transform.header
    pose.pose.position.x = transform.transform.translation.x
    pose.pose.position.y = transform.transform.translation.y
    pose.pose.position.z = transform.transform.translation.z
    pose.pose.orientation = transform.transform.rotation
    return pose

def transform_callback(msg):
    pose_msg = transform_to_pose(msg)
    pose_pub.publish(pose_msg)

if __name__ == '__main__':
    rospy.init_node('transform_to_pose_node')

    pose_pub = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=10)
    rospy.Subscriber('/vicon/modalai/modalai', TransformStamped, transform_callback)

    rospy.spin()
