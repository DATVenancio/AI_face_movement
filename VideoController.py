import imutils
from imutils.video import VideoStream
import cv2
class VideoController:
    def __init__(self):
        self.video_controller = VideoStream(src=0).start()

    def displayCamera(self):
        camera_frame = self.video_controller.read()
        camera_frame = imutils.resize(camera_frame,width=1200)
        return camera_frame

    def writeResults(self,frame,glasses_prediction):
        text_background_color = (0,0,0)
        cv2.rectangle(frame, (400, 10), (800, 60),text_background_color, thickness=-1)

        
        (down,idle,left,right,up) = glasses_prediction

        predominant_value=glasses_prediction.max()
        predominant_index =0
        for index in range(5):
            if(predominant_value==glasses_prediction[index]):
                predominant_index=index
        labels =["face_down","face_idle","face_left","face_right","face_up"]
        predominant_label = labels[predominant_index]
            
        
        cv2.putText(frame, predominant_label, (450,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),4)
    
    def showWindow(self,camera_frame):
        cv2.imshow("Frame",camera_frame)
        cv2.moveWindow("Frame",0,0)