#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_controller_py>"
    exit 1
fi

# Change directory to the parent directory
cd ..

# Source the setup.bash script for your ROS workspace
source devel/setup.bash

# Launch the ROS launch file in a new terminal
gnome-terminal -- roslaunch kinova_moveit demo_pick_and_place.launch &

# Run the Python script with the provided path in another new terminal
gnome-terminal -- python3 "$1" &
