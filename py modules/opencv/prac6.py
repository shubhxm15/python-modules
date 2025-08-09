import cv2 as cv
import numpy as np

kernel = np.ones([1,1], np.uint8)

vid = cv.VideoCapture(0)

while True:
    try:
        res, frame = vid.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)          # converting the vid into grayscale
        gray_vid = cv.Canny(frame, 150, 200)                   # converting the vid into edges
        erode_vid = cv.erode(gray_vid, kernel, iterations=1)   # erosion image to make the edging better
      # dilate_vid = cv.dilate(gray_vid, frame, iterations=1)  # dilate to increase the width of an image or vid
        cv.imshow('Sample edge video', erode_vid)
    except:
        pass

    if cv.waitKey(1) & 0xff==ord('q'):
        break
cv.destroyAllWindows()