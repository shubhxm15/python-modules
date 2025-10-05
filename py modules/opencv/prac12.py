import cv2 as cv
import easyocr as ocr
import matplotlib.pyplot as plt

path = "opencv/images/1_3.webp"

image = cv.imread(path)

read = ocr.Reader(['en'], gpu=True)   # cuda is not installed in my case

text_ = read.readtext(image)

for t in text_:
    print(t)

    bbox, text, score = t

    cv.rectangle(image, bbox[0], bbox[2], (0, 255, 0), 3)  # drawing rectangle through the text
    cv.putText(image, text, bbox[0], cv.FONT_HERSHEY_COMPLEX , 0.8, (255, 0, 0), 2)  # putting text in the image

plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))   # converted shown image into rgb
plt.show()