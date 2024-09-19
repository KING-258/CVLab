import cv2
import numpy as np
image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
equalized_image = clahe.apply(image)
gequ_image = cv2.equalizeHist(image)
cv2.imshow('Original Image', image)
cv2.imshow('Locally Equalized Image', equalized_image)
cv2.imshow('Globally Equalized Image', gequ_image)
cv2.waitKey(0)
cv2.destroyAllWindows()