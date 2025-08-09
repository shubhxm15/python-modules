import cv2

img = cv2.imread('opencv\demo.jpg')

img = cv2.resize(img, (500, 600))          # to resize the image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # to convert the image color to grayscale or black&white

cv2.imshow('grayscale', gray)
cv2.waitKey(0)                          # imp steps to show the image 
cv2.destroyAllWindows()