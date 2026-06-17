from ultralytics import YOLO
import cv2

print("Loading YOLO model...")

# Load YOLOv8 model
object_detector = YOLO("yolov8n.pt")

# Input video path
input_video_path = "input_videos/sample_video.mp4"

video_capture = cv2.VideoCapture(input_video_path)

# Check video
if not video_capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Video properties
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Fix FPS issue
if video_fps == 0:
    video_fps = 30

print("Video opened:", video_capture.isOpened())
print("Width:", frame_width)
print("Height:", frame_height)
print("FPS:", video_fps)

# Output path
output_video_path = "output_videos/tracked_output.mp4"

video_writer = cv2.VideoWriter(
    output_video_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    video_fps,
    (frame_width, frame_height)
)

processed_frames = 0

print("Starting object detection and tracking...")

while True:

    frame_available, frame = video_capture.read()

    if not frame_available:
        break

    processed_frames += 1

    # Object detection + tracking
    results = object_detector.track(
        frame,
        persist=True,
        verbose=False
    )

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Write frame
    video_writer.write(annotated_frame)

video_capture.release()
video_writer.release()

print(f"Total frames processed: {processed_frames}")
print("Tracking completed successfully!")
print(f"Output saved at: {output_video_path}")