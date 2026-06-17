# 🎯 Object Detection and Tracking System

## Overview

This project was developed as part of the CodeAlpha Artificial Intelligence Internship Program.

The Object Detection and Tracking System uses the YOLOv8 deep learning model to identify and track objects in video streams. The system can detect multiple object classes such as people, cars, buses, trucks, bicycles, and motorcycles while maintaining object tracking across frames.

The processed video is saved with bounding boxes and tracking information, providing a practical computer vision solution for surveillance, traffic monitoring, and video analytics.

---

## Features

* Real-time object detection using YOLOv8
* Multi-object tracking across video frames
* Support for multiple object classes
* Video processing using OpenCV
* Interactive Streamlit interface
* Download processed output videos
* High accuracy and fast inference

---

## Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy
* Streamlit

---

## Project Structure

CodeAlpha_ObjectDetectionTracking/

├── app.py

├── detect_and_track.py

├── requirements.txt

├── README.md

│

├── input_videos/

├── output_videos/

└── screenshots/

---

## Workflow

1. Upload a video.
2. YOLOv8 detects objects in each frame.
3. Object tracking assigns IDs and follows objects across frames.
4. Bounding boxes are drawn on detected objects.
5. Processed video is saved and made available for download.

---

## Applications

* Traffic Monitoring
* Smart Surveillance
* Crowd Analysis
* Vehicle Tracking
* Security Systems
* Smart City Solutions

---

## Results

* Successfully processed 900 video frames.
* Generated tracked output videos with object annotations.
* Implemented object detection and tracking using state-of-the-art YOLOv8 architecture.

---

## Author

Vishal Kumar

B.Tech CSE (AI & ML)

Graphic Era Deemed to be University

Developed as part of the CodeAlpha Artificial Intelligence Internship Program.
