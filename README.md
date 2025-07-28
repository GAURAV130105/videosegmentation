# 🎯 Real-Time Object Detection with YOLOv8 + OpenCV

This Python script uses Ultralytics YOLOv8 to perform real-time object detection on a video file. It displays results live in an OpenCV window and can optionally save the processed video with bounding boxes.

## 📁 Project Structure
- yolo_video_detection.py       # This script
- messsiiiii.mp4                # Input video file
- yolo11n.pt                    # YOLOv8 model file
- output.mp4                    # [Optional] Saved output video

## 🚀 Features
- ✅ Real-time object detection using YOLOv8
- ✅ Resizable OpenCV output window
- ✅ Optional saving of output video with annotations
- ✅ Lightweight and customizable

## 🔧 Requirements

Install dependencies:

    pip install ultralytics opencv-python

## ▶️ How to Use

1. Place your input video (e.g., `messsiiiii.mp4`) and YOLO model (`yolo11n.pt`) in the same folder.
2. Run this script:

    python yolo_video_detection.py

3. Press `q` or close the window to stop the detection.

## ⚙️ Configuration Options

You can modify these values in the script:

| Variable        | Description                                 |
|----------------|---------------------------------------------|
| `input_video`   | Path to your input video file               |
| `model_path`    | YOLOv8 model file (.pt)                     |
| `output_size`   | Frame size for display and output video     |
| `save_output`   | Set to `True` to save output video          |

---

👤 Author: **Gaurav**
