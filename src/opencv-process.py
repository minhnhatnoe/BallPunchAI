import cv2
import numpy as np
import configs, tools

def process_video(video_name: str) -> bool:
    data_array = tools.load_data(video_name)
    video_path = tools.get_video_path(video_name)
    video_capture = cv2.VideoCapture(video_path)
    read_successful, image = video_capture.read()
    cv2.namedWindow(video_name)
    cv2.moveWindow(video_name, 0, 0)
    count = 0
    for _ in data_array:
        if read_successful == False:
            break
        read_successful, image = video_capture.read()
        count += 1

    while read_successful:
        image_small = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow(video_name, image_small)
        state = cv2.waitKey()
        if state == 49:  # 1
            data_array.append(False)
        elif state == 48:  # 0
            data_array.append(True)
        elif state == 27 or state == -1: # Escape or AltF4
            print("Exiting")
            exit(0)
        else:
            data_array.pop()
            print(f"{state} pressed. Reverting")
            tools.flush_data(video_name, data_array)
            return True
        if count % 100 == 0:
            tools.flush_data(video_name, data_array)
        read_successful, image = video_capture.read()
        count += 1
    tools.flush_data(video_name, data_array)
    cv2.destroyWindow(video_name)
    return False


for video_name in configs.process_queue:
    not_success = True
    while not_success:
        not_success = process_video(video_name)

