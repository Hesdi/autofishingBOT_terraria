import time
import cv2
import mss
import numpy as np
from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}

def screen_record_efficient():
    cur = queryMousePosition()
    mon = {"top": cur['y'], "left": cur['x'], "width": 100, "height": 100}

    title = '[MSS] FPS benchmark'
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while True:
        img = np.asarray(sct.grab(mon))
        fps +=1

        cv2.imshow(title, img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return fps

print('Mss:', screen_record_efficient())
