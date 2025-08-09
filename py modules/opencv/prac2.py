import cv2

img = cv2.imread('opencv\demo.jpg')
img = cv2.resize(img, (500, 600))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # converts the image to hsv which helps in color detection
                                              # hsv - hue saturation value(of brightness)
cv2.imshow('hsv convert', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
