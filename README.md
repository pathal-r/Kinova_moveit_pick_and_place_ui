# Kinova MoveIt! Pick and Place UI

This repository contains a Gazebo simulation, RViz integration, and a MoveIt! plugin for the Kinova arm. The setup uses the xacro files provided by the manufacturer. This README will guide you through the steps to set up and run the simulation and UI.

## Prerequisites

Before starting, ensure you have the following installed on your system:
- ROS (Robot Operating System)
- Gazebo
- RViz
- MoveIt!
- catkin tools

## Setup Instructions

1. **Create a Workspace**

   Open a terminal and create a new directory for the workspace:

   ```bash
   mkdir -p ~/kinova_ws/src
   cd ~/kinova_ws/src

2. **Copy Repository Contents**

  Clone this repository and copy the src, scripts, and UI folders to the workspace:

  '''bash
  git clone <your-repo-url> kinova_moveit_pick_and_place_ui
  cp -r kinova_moveit_pick_and_place_ui/src .
  cp -r kinova_moveit_pick_and_place_ui/scripts .
  cp -r kinova_moveit_pick_and_place_ui/UI . 

3. **Build the Workspace**

  Navigate to the workspace root and build the workspace using catkin_make:

  '''bash
  cd ~/kinova_ws
  catkin_make

4. **Run the Controller Script**

  Navigate to the scripts directory and execute the controller script:

  '''bash
  cd ~/kinova_ws/scripts
  ./run_controller.sh scripth_path:= ~/kinova_ws/UI


## Demo Video 
  
   To see the demo of the Kinova MoveIt! Pick and Place UI in action, check out the video below (To watch full video go to resources folder):

   ![Demo_video-ezgif com-video-to-gif-converter](https://github.com/pathal-r/Kinova_moveit_pick_and_place_ui/assets/123066048/178b007d-da5b-430c-ba2b-b0100828564e)


   
