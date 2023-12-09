from keras.models import load_model
import cv2
from VideoController import VideoController
from FaceMovementDetector import FaceMovementDetector
from KeyboardSimulator import KeyboardSimulator


glasses_detector_model = load_model("face_movement.model")
video_controller = VideoController()
face_movement_detector = FaceMovementDetector()
keyboard_simulator = KeyboardSimulator()
while True:
    camera_frame=video_controller.displayCamera()
    glasses_prediction = face_movement_detector.detectGlasses(camera_frame,glasses_detector_model)[0]
    video_controller.writeResults(camera_frame,glasses_prediction)
    keyboard_simulator.simulate(glasses_prediction)
    video_controller.showWindow(camera_frame)

    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()
video_controller.stop()