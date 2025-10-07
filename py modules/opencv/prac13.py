import mediapipe as mp
import cv2 as cv

# cam = cv.VideoCapture(0)

# while cam.isOpened():
#     ret, frame = cam.read()
#     cv.imshow('web cam', frame)

#     if cv.waitKey(10) & 0xff == ord('q'):
#         break

# cam.release()
# cv.destroyAllWindows()

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cam = cv.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:

    while cam.isOpened():
        ret, frame = cam.read()
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = holistic.process(img)
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
        mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)  

        cv.imshow('holistic cam', img)

        if cv.waitKey(10) & 0xff == ord('q'):
            break

cam.release()
cv.destroyAllWindows()