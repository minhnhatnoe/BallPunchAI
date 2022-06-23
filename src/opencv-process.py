import cv2
paths = ["VID3", "VID2", "VID4", "VID5", "VID6"]
a_folder = "Dataset\\Punch"
b_folder = "Dataset\\NotPunch"
for name in paths:
    path = f"Dataset\\{name}.mp4"
    video_capture = cv2.VideoCapture(path)
    success,image = video_capture.read()
    index = 0
    cv2.namedWindow("X")
    while success:
        success,image = video_capture.read()
        img_name = f"{name}_{index}"
        imagesmall = cv2.resize(image, (0, 0), fx = 0.2, fy = 0.2)

        cv2.imshow("X", image)
        state = cv2.waitKey()
        print(state)
        while True:
            if state == 13:
                # Enter
                cv2.imwrite(f"{a_folder}\\{img_name}.png", image)
                break
            elif state == 32:
                # Space
                cv2.imwrite(f"{b_folder}\\{img_name}.png", image)
                break
            state = cv2.waitKey()
        index+=1
