import numpy as np
import cv2 as cv
from prac7 import set_limits
from PIL import Image

cam = cv.VideoCapture(0)
yellow = [0, 255, 255]

while True:
    
    ret, frame = cam.read()
    hsvimg = cv.cvtColor(frame, cv.COLOR_BGR2HSV)    # converting frane to hsv

    lower_limit, upper_limit = set_limits(color=yellow)    
                                                           # assigning limits for color 
    mask = cv.inRange(hsvimg, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1,y1), (x2,y2), [0, 255, 0], 3)    # forming rectangle to show the yellow color inside that rectangle
        cv.putText(frame, 'Yellow Color', (x1,y1), cv.FONT_HERSHEY_COMPLEX, 1, [0, 255, 0])

    cv.imshow('frame', frame)
        
    if cv.waitKey(1) & 0xff==ord('q'):
        break

cam.release()
cv.destroyAllWindows()