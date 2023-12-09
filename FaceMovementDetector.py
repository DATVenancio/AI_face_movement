from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

class FaceMovementDetector:
    def detectGlasses(self,frame,mask_model):
        faces =[]
        preds =[]
        (frame_height,frame_width)=frame.shape[:2]
        face=frame[0:]
        face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
        face = cv2.resize(face,(224,224))
        face=img_to_array(face)
        face=preprocess_input(face)

        faces.append(face)
        faces=np.array(faces,dtype="float32")

        preds = mask_model.predict(faces,batch_size=32)
        return preds