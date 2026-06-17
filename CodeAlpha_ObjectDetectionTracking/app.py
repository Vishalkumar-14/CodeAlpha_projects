import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="Object Detection & Tracking",
    page_icon="🎯",
    layout="centered"
)

# Create folders automatically
os.makedirs("input_videos", exist_ok=True)
os.makedirs("output_videos", exist_ok=True)

st.title("🎯 Object Detection and Tracking")

st.write(
    """
    Upload a video and run YOLOv8 object detection and tracking.
    The processed video will be available for download after analysis.
    """
)

st.divider()

uploaded_video = st.file_uploader(
    "Upload a Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:

    input_video_path = "input_videos/sample_video.mp4"

    with open(input_video_path, "wb") as video_file:
        video_file.write(uploaded_video.read())

    st.success("Video uploaded successfully!")

    if st.button("Start Detection & Tracking"):

        with st.spinner("Processing video... Please wait."):

            process = subprocess.run(
                ["python", "detect_and_track.py"],
                capture_output=True,
                text=True
            )

        if process.returncode == 0:

            output_video_path = (
                "output_videos/tracked_output.mp4"
            )

            if os.path.exists(output_video_path):

                st.success(
                    "Object detection and tracking completed successfully!"
                )

                with open(
                    output_video_path,
                    "rb"
                ) as processed_video:

                    st.download_button(
                        label="📥 Download Processed Video",
                        data=processed_video,
                        file_name="tracked_output.mp4",
                        mime="video/mp4"
                    )

            else:

                st.error(
                    "Processing finished but output video was not found."
                )

        else:

            st.error(
                "An error occurred during processing."
            )

            st.code(
                process.stderr
            )