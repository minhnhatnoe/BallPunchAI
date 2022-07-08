import cv2
import numpy as np
import configs, tools

def process_video(video_name: str) -> bool:
    video_path = tools.get_video_path(video_name)
    video_capture = cv2.VideoCapture(video_path)
    read_successful, image = video_capture.read()
    video_array = []
    while read_successful:
        image = cv2.resize(image, (256, 256))
        video_array.append(image)
        read_successful, image = video_capture.read()
    video_array = np.array(video_array)
    print(f"Flushing {video_name}")
    tools.flush_data(f"{video_name}_Extract", video_array)


for video_name in configs.process_queue:
    print(f"Extracting {video_name}")
    process_video(video_name)
