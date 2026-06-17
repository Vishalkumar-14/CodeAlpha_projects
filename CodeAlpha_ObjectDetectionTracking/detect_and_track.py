import streamlit as st
import subprocess
import os
import sys

st.set_page_config(
    page_title="Object Detection & Tracking",
    page_icon="🎯",
    layout="centered"
)

# Create folders if they don't exist
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

        current_directory = os.path.dirname(
            os.path.abspath(__file__)
        )

        tracking_script_path = os.path.join(
            current_directory,
            "detect_and_track.py"
        )

        if not os.path.exists(tracking_script_path):
            st.error(
                f"detect_and_track.py not found.\n\nExpected path:\n{tracking_script_path}"
            )
            st.stop()

        with st.spinner("Processing video... Please wait."):

            process = subprocess.run(
                [sys.executable, tracking_script_path],
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
                    "Processing completed but output video was not generated."
                )

        else:

            st.error(
                "An error occurred during processing."
            )

            st.code(process.stderr)