import cv2
import tools

def process_video(video_name: str) -> bool:
    video_path = tools.get_video_path(video_name)
    video_capture = cv2.VideoCapture(video_path)
    read_successful, image = video_capture.read()
    cnt = 0
    while read_successful:
        cv2.imwrite(f"export/{video_name}/frame_{cnt:06d}.png", image)
        cnt += 1
        read_successful, image = video_capture.read()


for video_name in ["VID1", "VID3", "VID4", "VID5", "VID6"]:
    print(f"Extracting {video_name}")
    process_video(video_name)
