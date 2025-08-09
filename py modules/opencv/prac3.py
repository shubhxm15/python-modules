import cv2 as cv

video = cv.VideoCapture(0)  # to open webcam

while True:
    try:
        res, frame = video.read()
        cv.imshow('sample video', frame)      

    except:
        pass

    if cv.waitKey(1) & 0xff==ord('q'):
        break

cv.destroyAllWindows()