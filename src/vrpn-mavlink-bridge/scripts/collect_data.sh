#!/bin/bash

# Set the output directory and filename
output_dir="/home/root/rosbags"
output_filename="data_$(date +%Y%m%d_%H%M%S).bag"

# Start rosbag record
rosbag record -O "$output_dir/$output_filename" /mavros/local_position/odom /mavros/rc/out /mavros/vision_pose/pose
