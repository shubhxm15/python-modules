import cv2 as cv

face_detection = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv.VideoCapture(0)

while True:
    _, img = cam.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.1, 3)

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), [0, 255, 255], 3)
    

    cv.putText(img, 'face detected', (w,h), cv.FONT_HERSHEY_COMPLEX, 1, [0, 255, 0])
    cv.imshow('Face detection', img)


    if cv.waitKey(1) & 0xff==ord('q'):
        break

cam.release()
cv.destroyAllWindows()