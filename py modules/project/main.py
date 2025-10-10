import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 360)

while True:
    success, img = cap.read()
    # img = cv.flip(img, 1)
    hand, img = detector.findHands(img)

    if hand and hand[0]['type'] == 'Right':
        fingers = detector.fingersUp(hand[0])
        totalfingers = fingers.count(1)

        cv.putText(img, f'Fingers: {totalfingers}', (20, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        if totalfingers == 5:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        elif totalfingers == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

    cv.imshow('Hand detector', img)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
