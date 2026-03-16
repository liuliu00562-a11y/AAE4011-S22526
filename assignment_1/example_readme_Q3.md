# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** Liu Pui Ling | **Student ID:** 25134783D | **Date:** 17/3

---

## 1. Overview

This project uses ROS 2 to read a video from a rosbag file and uses an AI model to detect vehicles and pedestrians in real-time. It acts as the "eyes" for a robot or drone to understand road safety.

## 2. Detection Method *(Q3.1 — 2 marks)*

I chose the **YOLOv8** (yolov8n.pt) model. I selected this model because it is very fast and lightweight. It is perfect for real-time video processing on a regular computer without slowing down the ROS 2 system.

## 3. Repository Structure

My ROS 2 package is structured like this:

```text
ros2_ws/
├── src/
│   └── vehicle_detector/
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── vehicle_detector/
│           ├── __init__.py
│           └── detector_node.py (Main Python script)
└── data/
    └── teacher_video_1/ (Converted rosbag file)

```

## 4. Prerequisites

To run this project, you need the following software and libraries:

* **Operating System:** Ubuntu (via Windows WSL)
* **ROS Version:** ROS 2 (Jazzy)
* **Python Version:** Python 3.12
* **Key Libraries:** `ultralytics` (for YOLO), `opencv-python` (for images), `numpy`, `sensor_msgs` (for handling CompressedImage).

## 5. How to Run *(Q3.1 — 2 marks)*

1. **Clone/Create the repository:** Place the `vehicle_detector` package into your `~/ros2_ws/src` folder.
2. **Install dependencies:** Run `pip3 install ultralytics opencv-python --break-system-packages` in the Ubuntu terminal.
3. **Build the ROS package:** Open Terminal 1 and type:
```bash
cd ~/ros2_ws
colcon build --packages-select vehicle_detector
source install/setup.bash

```


4. **Place the rosbag file:** Use `rosbags-convert` to change the old ROS 1 bag into a ROS 2 format, and place it in `~/ros2_ws/data/teacher_video_1`.
5. **Launch the pipeline:** * In **Terminal 1**, start the AI node:
```bash
export DISPLAY=:0
ros2 run vehicle_detector detector_node

```


* In **Terminal 2**, play the video data:
```bash
cd ~/ros2_ws/data
ros2 bag play teacher_video_1

```





## 6. Sample Results

* **Total frames:** 1142
* **Resolution:** 512x640
* **Topic name:** `/hikcamera/image_2/compressed`
* **Detection statistics:** Processing time is very fast, taking about 15ms to 30ms per frame. The AI successfully detects multiple cars, buses, and persons in a single frame in real-time.
* ![WhatsApp Image 2026-03-17 at 05 17 13](https://github.com/user-attachments/assets/40e59225-7389-4538-af7c-785499f3a392)

## 7. Video Demonstration *(Q3.2 — 5 marks)*

**Video Link:** https://youtu.be/AJ2MCdwhWXI

*The video shows Terminal 1 acting as the processor (running the AI) and Terminal 2 acting as the data provider (playing the rosbag). The AI window displays bounding boxes and labels for cars and pedestrians in real-time.*

## 8. Reflection & Critical Analysis *(Q3.3 — 8 marks)*

### (a) What Did You Learn? *(2 marks)*

First, I learned how to use the ROS 2 "Publisher and Subscriber" architecture. I learned how to subscribe to a specific topic (`/hikcamera/image_2/compressed`) to get data. Second, I learned how to integrate an AI model (YOLOv8) into a ROS 2 Python node and decode `CompressedImage` messages into regular images using `numpy` and OpenCV.

### (b) How Did You Use AI Tools? *(2 marks)*

I used an AI assistant to help me troubleshoot errors and write the Python node. **Benefits:** The AI was very helpful in solving path issues in Windows WSL (Ubuntu) and fixing the "RCLError" and display missing errors. **Limitations:** The AI cannot see my screen, so I had to carefully copy and paste the exact terminal outputs and file names so it could give me the correct commands.

### (c) How to Improve Accuracy? *(2 marks)*

1. **Train on a specific dataset:** We can train the YOLO model on a custom dataset of drone images (top-down view). Right now, the pre-trained model is trained on normal camera views, so a top-down dataset would make it smarter for drone flying.
2. **Use a larger model:** Instead of using the small `yolov8n.pt` model, we could use a larger model like `yolov8m.pt` (Medium). It requires more computing power but is much more accurate at finding small objects.

### (d) Real-World Challenges *(2 marks)*

Deploying this on an actual drone has two main challenges. **First, computing power:** Drones have small batteries, and running heavy AI models uses a lot of power and generates heat. **Second, environmental factors:** Real-time detection from a moving drone is affected by motion blur, rain, and changing sunlight, which makes it much harder for the AI to see clearly compared to a recorded video.

## 9. References

* ROS 2 Jazzy Documentation: https://docs.ros.org/en/jazzy/
* Ultralytics YOLOv8 Documentation: https://docs.ultralytics.com/
* OpenCV Python Tutorials: https://docs.opencv.org/

```

Is there anything else you need me to adjust before you submit it?

```
