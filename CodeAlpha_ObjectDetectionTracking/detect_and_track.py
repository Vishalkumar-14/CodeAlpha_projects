from ultralytics import YOLO
import cv2
import os

print("Loading YOLO model...")

# Get current project directory
current_directory = os.path.dirname(
    os.path.abspath(__file__)
)

# Create folders if they don't exist
input_folder = os.path.join(
    current_directory,
    "input_videos"
)

output_folder = os.path.join(
    current_directory,
    "output_videos"
)

os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Input and output paths
input_video_path = os.path.join(
    input_folder,
    "sample_video.mp4"
)

output_video_path = os.path.join(
    output_folder,
    "tracked_output.mp4"
)

print("Input Video:", input_video_path)
print("Output Video:", output_video_path)

# Load YOLOv8 model
object_detector = YOLO("yolov8n.pt")

# Open video
video_capture = cv2.VideoCapture(
    input_video_path
)

if not video_capture.isOpened():

    print(
        "Error: Unable to open video file."
    )

    exit()

# Video properties
frame_width = int(
    video_capture.get(
        cv2.CAP_PROP_FRAME_WIDTH
    )
)

frame_height = int(
    video_capture.get(
        cv2.CAP_PROP_FRAME_HEIGHT
    )
)

video_fps = int(
    video_capture.get(
        cv2.CAP_PROP_FPS
    )
)

if video_fps == 0:
    video_fps = 30

print("Video opened:", video_capture.isOpened())
print("Width:", frame_width)
print("Height:", frame_height)
print("FPS:", video_fps)

# Video writer
video_writer = cv2.VideoWriter(
    output_video_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    video_fps,
    (frame_width, frame_height)
)

processed_frames = 0

print(
    "Starting object detection and tracking..."
)

while True:

    frame_available, frame = (
        video_capture.read()
    )

    if not frame_available:
        break

    processed_frames += 1

    # Run tracking
    results = object_detector.track(
        frame,
        persist=True,
        verbose=False
    )

    # Draw detections
    annotated_frame = (
        results[0].plot()
    )

    # Save frame
    video_writer.write(
        annotated_frame
    )

video_capture.release()
video_writer.release()

print(
    f"Total frames processed: {processed_frames}"
)

print(
    "Tracking completed successfully!"
)

print(
    f"Output saved at: {output_video_path}"
)