import os
from imutils.video import VideoStream
import cv2
import time


chosen_class = input("enter the class initial: ")
chosen_map = {'d': 'face_down', 'i': 'face_idle', 'l': 'face_left','r':'face_right','u':'face_up'}

os.chdir("dataset/"+chosen_map.get(chosen_class))


vs = VideoStream(src=0).start()

time.sleep(1.0)
start_time = time.time()
for count in range(100):
    frame = vs.read()
    filename = str(count)+str(start_time)+".png"
    cv2.imwrite(filename, frame)
    time.sleep(0.01)

print("final!")
cv2.destroyAllWindows()
vs.stop()
