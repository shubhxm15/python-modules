import cv2 as cv

vid = cv.VideoCapture(0)

while True:
    try:
        res, frame = vid.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        edge_vid = cv.Canny(frame, 150, 200)
        cv.imshow('gray video', edge_vid)
    except:
        pass

    if cv.waitKey(3) & 0xff==ord('q'):
        break
    
cv.destroyAllWindows()