import streamlit as st
import cv2
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("YOLOv8 Object Detection in Video")

# Load YOLO model
model = YOLO("yolo11n.pt")

# Load video
video_path = "messsiiiii.mp4"
cap = cv2.VideoCapture(video_path)

frame_placeholder = st.empty()

# Run through video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model.predict(source=frame, save=False, verbose=False)
    result_frame = results[0].plot()

    # Convert for Streamlit display
    result_rgb = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(result_rgb, channels="RGB", use_column_width=True)
    
cap.release()
