
import random
import cv2
#import numpy as np
from ultralytics import YOLO
import threading
from playsound import playsound

Alarm_Status = False
Fire_Reported = 0

def play_alarm_sound_function():
	while True:
         playsound('Alarm.mp3',True)

# opening the file in read mode
my_file = open("utils/coco.txt", "r")
# reading the file
data = my_file.read()
# replacing end splitting the text | when newline ('\n') is seen.
class_list = data.split("\n")
my_file.close()

# print(class_list)

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# load a pretrained YOLOv8n model
model = YOLO("best (2).pt")

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480

cam = cv2.VideoCapture(0)

## visualiser une image

while True:
    (grabbed, frame) = cam.read()
    if not grabbed:
        break

    detect_params = model.predict(source=[frame], conf=0.25, save=False)

    # Convert tensor array to numpy


    DP = detect_params[0].numpy()
    print(DP)


    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            print(i)

            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box

            clsID = box.cls.numpy()[0]

            conf = box.conf.numpy()[0]

            bb = box.xyxy.numpy()[0]


            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (0, 0, 0),
                2,
            )


    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    if Fire_Reported >= 1:
        if Alarm_Status == False:
            threading.Thread(target=play_alarm_sound_function).start()
            Alarm_Status = True
    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()
