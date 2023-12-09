import time
from pynput.keyboard import Controller
class KeyboardSimulator:
    def simulate(self,prediction):
        keyboard=Controller()
        (down,idle,left,right,up) = prediction
        prediction_map = {down:'1',idle:None,left:'2',right:'3',up:'4'}
        maximun_prediction= max(prediction)
        if(prediction_map.get(maximun_prediction)):
            keyboard.press(prediction_map.get(maximun_prediction))
            time.sleep(0.2)
            keyboard.release(prediction_map.get(maximun_prediction))

