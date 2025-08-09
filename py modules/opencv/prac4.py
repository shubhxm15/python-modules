import cv2 as cv

img = cv.imread('opencv\demo.jpg')
img=  cv.resize(img, (500, 600))

grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow('sample', grayimg)
cv.waitKey(0)
cv.destroyAllWindows()

edgeimg = cv.Canny(grayimg, 150, 200)   # will only show edges in the image

cv.imshow('edge sample', edgeimg)
cv.waitKey(0)
cv.destroyAllWindows()