import json
from os import path
import cv2

dataset_path = path.realpath(path.join(path.realpath(__file__), path.pardir, "Dataset"))
video_folder_path = path.realpath(path.join(dataset_path, "videos"))
json_file_path = path.join(dataset_path, "split.json")

data_dict = {}
def load_data() -> None:
    global data_dict
    with open(json_file_path, "r") as data_file:
        data_dict = json.load(data_file)

def flush_data() -> None:
    with open(json_file_path, "w") as data_file:
        json.dump(data_dict, data_file)

load_data()

process_queue = ["VID1", "VID2", "VID3", "VID4", "VID5", "VID6"]
for video_name in process_queue:
    if not video_name in data_dict:
        data_dict[video_name] = {}
    
    video_path = path.join(video_folder_path, f"{video_name}.mp4")
    video_capture = cv2.VideoCapture(video_path)
    read_succesful, image = video_capture.read()
    cv2.namedWindow(video_name)
    cv2.moveWindow(video_name, 0, 0)
    count = 0
    skipping = max(0, len(data_dict[video_name])-1)
    for _ in range(skipping):
        if read_succesful == False:
            break
        read_succesful, image = video_capture.read()
        count += 1

    while read_succesful:
        image_small = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow(video_name, image_small)
        state = cv2.waitKey()
        if state == 32: # Space
            data_dict[video_name][str(count)] = False
        elif state == 13: # Enter
            data_dict[video_name][str(count)] = True
        else:
            print("Invalid key pressed. Flushing data and exiting")
            flush_data()
            exit(0)
        if count % 100 == 0:
            flush_data()
        read_succesful, image = video_capture.read()
        count += 1
    cv2.destroyWindow(video_name)
