# Kinova MoveIt! Pick and Place UI

This repository contains a Gazebo simulation, RViz integration, and a MoveIt! plugin for the Kinova arm. The setup uses the xacro files provided by the manufacturer. It uses ArUco marker tracking to get the position of the block and provides flexibility in the UI to choose between the OMPL planner and CHOMP planner provided by MoveIt. This README will guide you through the steps to set up and run the simulation and UI.


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
   ```
   

2. **Copy Repository Contents**

  Clone this repository and copy the src, scripts, and UI folders to the workspace:

  ```bash
  git clone https://github.com/pathal-r/Kinova_moveit_pick_and_place_ui kinova_moveit_pick_and_place_ui
  cp -r kinova_moveit_pick_and_place_ui/src ~/kinova_ws
  cp -r kinova_moveit_pick_and_place_ui/scripts ~/kinova_ws
  cp -r kinova_moveit_pick_and_place_ui/UI ~/kinova_ws
  ```

3. **Build the Workspace**

  Navigate to the workspace root and build the workspace using catkin_make:

  ```bash
  cd ~/kinova_ws
  catkin_make
  ```

4. **Run the Controller Script**

  Navigate to the scripts directory and execute the controller script:

  ```bash
  cd ~/kinova_ws/scripts
  ./run_controller.sh
  ```

## UI
   The UI for this project provides several buttons and checkboxes to control the Kinova arm and gripper. Below is a description of each element:

   - **OMPL Checkbox:** Makes the arm and gripper use the OMPL planner of MoveIt!
   - **CHOMP Checkbox:** Makes the arm and gripper use the CHOMP planner of MoveIt!
   - **Move to Initial Position:** Plans the trajectory from the current position to the home position defined as "ready" in the code.
   - **Move the Arm:** Plans the trajectory from the current position to the block's position using the tracking of an ArUco tag.
   - **Place on the Red Cylinder:** Plans the trajectory from the current position to the top of the red cylinder.
   - **Grab:** Plans the trajectory for the gripper to from the current state to the fully closed state.
   - **Open:** Plans the trajectory for the gripper to from the current state to the fully opened state.
   - **Pick and Place Button:** Plans the whole trajectory for the arm to pick the block, place it on the cylinder, and then return to the home position.


## Demo Video 
  
   To see the demo of the Kinova MoveIt! Pick and Place UI in action, check out the video below (To watch full video go to resources folder):

   ![Demo_video-ezgif com-video-to-gif-converter](https://github.com/pathal-r/Kinova_moveit_pick_and_place_ui/assets/123066048/178b007d-da5b-430c-ba2b-b0100828564e)


   
