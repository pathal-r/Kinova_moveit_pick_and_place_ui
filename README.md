# Kinova MoveIt Pick and Place UI

A ROS-based pick-and-place system for the Kinova robotic arm with ArUco marker tracking, MoveIt motion planning, and a PyQt5 control interface.

![Demo](https://github.com/pathal-r/Kinova_moveit_pick_and_place_ui/assets/123066048/178b007d-da5b-430c-ba2b-b0100828564e)

## Overview

This project provides a complete simulation pipeline for robotic pick-and-place operations using the Kinova arm. It integrates Gazebo simulation, RViz visualization, and MoveIt motion planning with a custom PyQt5 GUI that allows switching between OMPL and CHOMP planners. Object detection is handled through ArUco marker tracking for real-time block localization.

## Features

- Gazebo simulation with Kinova arm URDF/Xacro models
- ArUco marker-based object pose detection
- MoveIt integration with OMPL and CHOMP planner support
- Cartesian path planning for smooth arm trajectories
- PyQt5 GUI with individual and full pick-and-place controls
- ROS topic-based communication between perception and planning

## UI Controls

| Button | Action |
|--------|--------|
| OMPL / CHOMP | Switch motion planner |
| Move to Initial Position | Return arm to home pose |
| Move the Arm | Navigate to detected block |
| Place on Red Cylinder | Move to placement target |
| Grab / Open | Close or open gripper |
| Pick and Place | Execute full sequence |

## Tech Stack

`Python` · `ROS` · `MoveIt` · `Gazebo` · `RViz` · `PyQt5` · `OpenCV` · `ArUco`

## Prerequisites

- ROS (Noetic recommended)
- Gazebo
- MoveIt
- catkin tools

## Setup

```bash
mkdir -p ~/kinova_ws/src
cd ~/kinova_ws/src
git clone https://github.com/pathal-r/Kinova_moveit_pick_and_place_ui.git
cp -r Kinova_moveit_pick_and_place_ui/src ~/kinova_ws
cp -r Kinova_moveit_pick_and_place_ui/scripts ~/kinova_ws
cp -r Kinova_moveit_pick_and_place_ui/UI ~/kinova_ws
cp -r Kinova_moveit_pick_and_place_ui/aruco_block_long ~/.gazebo/models
cd ~/kinova_ws
catkin_make
```

## Run

```bash
cd ~/kinova_ws/scripts
./run_controller.sh
```

This launches Gazebo, RViz with MoveIt, and the PyQt5 controller UI.

## Project Structure

```
Kinova_moveit_pick_and_place_ui/
├── src/
│   ├── aruco_recognition/    # ArUco marker detection
│   ├── kinova_description/   # Robot URDF/Xacro files
│   └── kinova_moveit/        # MoveIt configuration and launch files
├── UI/                       # PyQt5 controller interface
├── scripts/                  # Launch scripts
├── aruco_block_long/         # Gazebo model for ArUco block
└── resources/                # Demo video
```
