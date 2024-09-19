import cv2
import numpy as np
image = cv2.imread('image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(gray, np.array([0]), np.array([150]))
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(mask, kernel, iterations=1)
details = cv2.connectedComponentsWithStats(dilated, connectivity=4)
print(f"Estimated word count: {details[0] -1}")
cv2.imshow('Segmented Image', mask)
cv2.imshow('Dilated Image', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()