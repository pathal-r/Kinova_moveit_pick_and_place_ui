#!/bin/bash

# Change directory to the parent directory
cd ..

# Source the setup.bash script for your ROS workspace
source devel/setup.bash

# Launch the ROS launch file in a new terminal
gnome-terminal -- roslaunch kinova_moveit demo_pick_and_place.launch &

# Run the Python script with the provided path in another new terminal
gnome-terminal -- python3 ~/kinova_ws/UI/controller.py
