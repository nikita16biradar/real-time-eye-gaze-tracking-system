# real-time-eye-gaze-tracking-system
A Python-based real-time eye gaze tracking system using OpenCV and MediaPipe for hands-free human-computer interaction.
# Real-Time Eye Gaze Tracking System

## Introduction

The Real-Time Eye Gaze Tracking System is a Python-based computer vision project that detects and tracks human eye movement using a webcam in real time. The system uses Artificial Intelligence and image processing techniques to estimate the direction of a user's gaze such as left, right, or center.

The project is developed using OpenCV and MediaPipe libraries. MediaPipe Face Mesh helps in detecting facial landmarks and iris positions accurately, while OpenCV handles webcam input, frame processing, and visualization.

This project demonstrates how eye movement can be used as a natural and touch-free method of interaction between humans and computers.

---

# Abstract

In modern computer systems, interaction is mainly performed using physical devices such as keyboards, mice, and touchscreens. These methods are not suitable for people with physical disabilities or limited motor abilities.

This project presents a low-cost and efficient real-time eye gaze tracking system that uses a standard webcam to detect eye movement and estimate gaze direction. The system captures live video frames, detects facial landmarks, tracks iris movement, and calculates gaze direction using computer vision techniques.

The project can be applied in assistive technology, driver monitoring systems, robotics, automation, and human-computer interaction systems.

---

# Problem Statement

Most computer systems depend on physical interaction devices such as keyboards and mice. These input methods create difficulties for physically disabled users and individuals with limited hand movement.

Existing eye-tracking systems are often expensive and require specialized hardware, making them inaccessible for many users.

Therefore, there is a need for a low-cost, webcam-based, real-time eye gaze tracking system that can enable touch-free interaction and improve accessibility.

---

# Objectives

- To develop a real-time eye gaze tracking system using Python
- To capture live video from a webcam
- To detect face and eye landmarks using MediaPipe
- To track iris movement accurately
- To estimate gaze direction such as left, right, and center
- To provide hands-free human-computer interaction
- To create a low-cost and accessible solution

---

# Scope of the Project

The project focuses on real-time eye movement detection using only a webcam and software-based computer vision techniques.

The system can be extended for:
- Cursor control using eye movement
- Driver attention monitoring
- Accessibility systems for disabled users
- Smart home automation
- Robotics control systems
- Human behavior analysis

---

# Technologies Used

| Technology | Description |
|------------|-------------|
| Python | Main programming language |
| OpenCV | Image processing and webcam handling |
| MediaPipe | Face mesh and iris landmark detection |
| NumPy | Mathematical operations and calculations |

---

# System Requirements

## Hardware Requirements

- Laptop/Desktop
- Webcam
- Minimum 4GB RAM
- Intel i3 or higher processor

## Software Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- VS Code / PyCharm

---

# Modules Description

## 1. main.py

This is the main execution file of the project. It starts webcam capture, processes video frames, and displays the final output.

## 2. gaze.py

This module contains the logic for eye tracking and gaze direction calculation.

## 3. utils.py

This file contains helper functions used for calculations, drawing landmarks, and visualization.

## 4. hand_gesture.py

This module handles hand gesture-related functionalities if integrated with the system.

## 5. head_pose.py

This module estimates head movement and orientation.

## 6. robot_control.py

This module can be used for controlling robotic systems using gaze direction.

---

# Working of the System

1. The webcam captures live video frames continuously.

2. OpenCV processes each frame and converts it into a suitable format.

3. MediaPipe Face Mesh detects facial landmarks.

4. Eye landmarks and iris points are extracted from the detected face mesh.

5. The iris position is analyzed relative to eye boundaries.

6. Mathematical calculations are performed to estimate gaze direction.

7. The final result is displayed on the screen with eye tracking visualization and FPS information.

---

# Project Architecture

```text
Webcam Input
      ↓
Frame Capture using OpenCV
      ↓
Face Detection using MediaPipe
      ↓
Eye Landmark Detection
      ↓
Iris Tracking
      ↓
Gaze Direction Calculation
      ↓
Output Visualization
```

---

# Features

- Real-time eye tracking
- Iris detection
- Gaze estimation
- Webcam-based system
- Live visualization
- FPS monitoring
- Hands-free interaction
- Easy to use
- Low-cost implementation

---

# Advantages

- No special hardware required
- Cost-effective solution
- Real-time performance
- Portable system
- Improves accessibility
- Easy to implement and use
- Can be integrated with AI systems

---

# Limitations

- Performance depends on lighting conditions
- Webcam quality affects accuracy
- Accuracy may reduce during rapid head movement
- Requires visible face positioning

---

# Applications

- Assistive technology for disabled users
- Driver monitoring systems
- Human-computer interaction
- Smart automation systems
- Robotics control
- Gaming systems
- Attention monitoring systems

---

# Future Enhancements

- Cursor control using eye movement
- Blink detection system
- Voice assistant integration
- Deep learning-based gaze estimation
- IoT device control
- Mobile application integration

---

# Installation Steps

## Step 1: Clone the Repository

```bash
git clone https://github.com/nikita16biradar/real-time-eye-gaze-tracking-system.git
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Run the Project

```bash
python main.py
```

---

# Output

The system displays:
- Facial landmarks
- Eye tracking points
- Iris position
- Gaze direction
- FPS counter

---

# Conclusion

The Real-Time Eye Gaze Tracking System successfully demonstrates the use of Artificial Intelligence and Computer Vision techniques for touch-free interaction.

The system provides an efficient, low-cost, and accessible solution for eye movement tracking using a webcam. It has significant applications in assistive technology, automation, driver monitoring, and human-computer interaction systems.

This project also shows how modern AI libraries such as OpenCV and MediaPipe can be used to build practical real-world solutions.

---

# Author

Nikita Biradar

GitHub:
https://github.com/nikita16biradar
