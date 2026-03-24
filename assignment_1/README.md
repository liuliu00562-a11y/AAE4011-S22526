# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** Liu Pui Ling | **Student ID:** 25134783D | **Date:** 2026-03-24

---

## 1. Overview 

This project uses ROS 2 to read a video from a rosbag file and uses an AI model to detect vehicles and pedestrians in real-time. Because the original data was in ROS 1 format, I created a conversion script to bridge the two systems. 

## 2. Detection Method
I chose the **YOLOv8** (yolov8n.pt) model. I selected this model because it is very fast and lightweight. It is perfect for real-time video processing on a regular computer without slowing down the ROS 2 system.

## 3. Repository Structure 

My ROS 2 package is structured like this. I have added the new conversion script here:

```text
ros2_ws/
├── src/
│   └── vehicle_detector/
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── vehicle_detector/
│           ├── __init__.py
│           ├── detector_node.py         (Main AI Python script)
│           └── convert_ros1_to_ros2.py  (ROS 1 to ROS 2 converter)
└── data/
    └── teacher_video_1/                 (Converted rosbag file )
````

## 4\. Prerequisites

To run this project, you need the following software and libraries:


  * **Operating System:** Ubuntu (via Windows WSL)
  * **ROS Version:** ROS 2 (Jazzy)
  * **Python Version:** Python 3.12
  * **Key Libraries:** `rosbags` (for conversion), `ultralytics` (for YOLO), `opencv-python`, `numpy`, `sensor_msgs`.

## 5\. How to Run
**Step 1: Convert the Data**
The assignment provided a ROS 1 bag. First, install the converter and change the file to ROS 2 format:

```bash
pip3 install rosbags ultralytics opencv-python --break-system-packages
python3 ~/ros2_ws/src/vehicle_detector/vehicle_detector/convert_ros1_to_ros2.py <input.bag> ~/ros2_ws/data/teacher_video_1
```

**Step 2: Build the ROS package **
Open Terminal 1 and type :

```bash
cd ~/ros2_ws
colcon build --packages-select vehicle_detector
source install/setup.bash
```

**Step 3: Launch the pipeline **

  * In **Terminal 1**, start the AI node :

<!-- end list -->

```bash
export DISPLAY=:0
ros2 run vehicle_detector detector_node
```

  * In **Terminal 2**, play the video data :

<!-- end list -->

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

## 7\. Video Demonstration  *(Q3.2)*

**Video Link:** https://youtu.be/AJ2MCdwhWXI

*The video shows Terminal 1 acting as the processor (running the AI) and Terminal 2 acting as the data provider (playing the rosbag). The AI window displays bounding boxes and labels for cars and pedestrians in real-time.*

## 8\. Reflection & Critical Analysis  *(Q3.3)*

### (a) What Did You Learn? 

Through this assignment, I gained two important technical skills. First, I learned how to use the ROS 2 "Publisher and Subscriber" architecture. I successfully wrote code to subscribe to the `/hikcamera/image_2/compressed` topic and decode `CompressedImage` messages into regular images using `numpy` and OpenCV. Second, I learned how to handle data format differences. Because the provided video was in ROS 1, I learned how to use the `rosbags` Python library to convert old `.bag` files into the new ROS 2 `.db3` format so my code could read it.

### (b) How Did You Use AI Tools? 

I used an AI assistant to help me troubleshoot errors and write parts of the Python code, including the conversion script. **Benefits:** The AI was extremely helpful in solving path issues in Windows WSL (Ubuntu) and fixing the "RCLError" and display missing errors. It explained how to fix my environment variables. **Limitations:** The AI cannot see my screen, so I had to carefully copy and paste the exact terminal outputs. Also, the AI sometimes gave me old ROS 1 code, so I had to double-check the code to make sure it was correct for ROS 2 Jazzy.

### (c) How to Improve Accuracy? 

1.  **Train on a specific drone dataset:** We can train the YOLO model on a custom dataset of drone images (top-down view). Right now, the pre-trained model is used to seeing things from a normal camera angle. A top-down dataset would make it much smarter for drone flying.
2.  **Use a larger model:** Instead of using the very small `yolov8n.pt` model, we could upgrade to a medium model like `yolov8m.pt`. It requires a stronger computer, but it is much more accurate at finding small objects from far away.

### (d) Real-World Challenges 

Deploying this on an actual drone has two main challenges. **First, computing power:** Drones run on small batteries. Running heavy AI models uses a lot of electricity and generates heat, which will shorten the drone's flight time. **Second, environmental factors:** Real-time detection from a moving drone is difficult because of motion blur, rain, and changing sunlight. It is much harder for the AI to see clearly in the real sky compared to a smooth, recorded video.

## 9\. References 

  * ROS 2 Jazzy Documentation: https://docs.ros.org/en/jazzy/
  * Ultralytics YOLOv8 Documentation: https://docs.ultralytics.com/
  * OpenCV Python Tutorials: https://docs.opencv.org/

<!-- end list -->
```
