from ultralytics import YOLO
import numpy as np
import streamlit as st
from PIL import Image

model = YOLO("yolov8n.pt")

st.set_page_config(
    page_title="Object Detection & Tracking",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Object Detection & Tracking System")

st.markdown(
    """
    Detect and identify real-world objects in images using
    **YOLOv8 (You Only Look Once)** and Computer Vision.
    """
)
st.write(
    "Upload an image and detect objects using YOLO."
)

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        caption="Input Image",
        use_container_width=True
    )

    if st.button("Detect Objects"):
        image_array = np.array(image)
        results = model(image_array)

        detected_classes = []
        detection_details = []
        detected_image = results[0].plot()
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            detected_classes.append(class_name)
            detection_details.append(
                {
                    "Object": class_name,
                    "Confidence": round(confidence * 100, 2)
                }
            )

        st.subheader("Detection Result")
        st.subheader("Detected Objects Summary")
        st.subheader("📊 Detection Statistics")
        st.subheader("📋 Detection Details")

        st.table(detection_details)
        # Display metrics and detected classes
        total_detected = len(detected_classes)
        unique_types = len(set(detected_classes))

        st.metric("Total Objects Detected", total_detected)
        st.metric("Unique Object Types", unique_types)

        if detected_classes:
            unique_classes = set(detected_classes)
            for obj in unique_classes:
                count = detected_classes.count(obj)
                st.write(f"• {obj}: {count}")
        else:
            st.write("No objects detected.")

        st.image(detected_image, caption="Detected Objects", use_container_width=True)