# 🎯 AI Object Detection & Tracking System

## 📌 Project Overview

The AI Object Detection & Tracking System is a computer vision application that detects and identifies objects in images using the YOLOv8 (You Only Look Once) deep learning model.

Users can upload an image through a Streamlit web interface, and the system automatically detects objects, draws bounding boxes, displays confidence scores, and provides detailed detection statistics.

This project demonstrates the practical application of Artificial Intelligence, Computer Vision, and Deep Learning for real-world object recognition tasks.

---

## 🚀 Features

- Upload images in JPG, JPEG, and PNG formats
- Object detection using YOLOv8
- Bounding boxes around detected objects
- Object labels with confidence scores
- Detection summary with object counts
- Detection statistics dashboard
- Detection details table
- Interactive Streamlit web interface
- Fast and accurate predictions

---

## 🛠️ Technologies Used

- Python
- Streamlit
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- Pillow

---

## 📂 Project Structure
CodeAlpha_ObjectDetectionTracking/
│
├── app.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository_url>
cd CodeAlpha_ObjectDetectionTracking

Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py

The application will open automatically in your browser.

📊 Working Process
Upload an image.
Click the Detect Objects button.
YOLOv8 processes the image.
Objects are detected and labeled.
Bounding boxes are displayed.
Detection statistics and confidence scores are shown.
🎯 Sample Output
Input Image
Dog
Car
Person
Bicycle
Output
Detected Objects
Confidence Scores
Object Count Summary
Detection Statistics
📈 Future Improvements
Real-time webcam detection
Video object tracking
Multi-object tracking
Object counting in live streams
Export detection reports
👨‍💻 Author

Neelima Kakulapati

CodeAlpha Artificial Intelligence Internship Project


---

### requirements.txt

Use:

```txt
streamlit
ultralytics
opencv-python
numpy
pillow