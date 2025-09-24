import cv2 as cv
import easyocr as ocr

path = "opencv/images/village-name-board-250x250.webp"

image = cv.imread(path)

read = ocr.Reader(['en'], gpu=True)

text = read.readtext(image)

print(text)