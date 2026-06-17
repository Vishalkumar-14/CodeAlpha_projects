import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="Object Detection & Tracking",
    page_icon="🎯"
)

st.title("🎯 Object Detection and Tracking")

st.write(
    """
    Upload a video, run YOLOv8 object detection and tracking,
    and download the processed video with bounding boxes.
    """
)

st.divider()

uploaded_video = st.file_uploader(
    "Upload a video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:

    input_path = "input_videos/sample_video.mp4"

    with open(input_path, "wb") as file:
        file.write(uploaded_video.read())

    st.success("Video uploaded successfully!")

    if st.button("Start Detection & Tracking"):

        with st.spinner("Processing video..."):

            subprocess.run(
                ["python", "detect_and_track.py"]
            )

        output_path = (
            "output_videos/tracked_output.mp4"
        )

        if os.path.exists(output_path):

            st.success(
                "Processing completed!"
            )

            with open(
                output_path,
                "rb"
            ) as video_file:

                st.download_button(
                    "Download Processed Video",
                    video_file,
                    file_name="tracked_output.mp4"
                )