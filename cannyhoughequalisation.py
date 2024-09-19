import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Step 1: Histogram Equalization
# Improve contrast in the image using histogram equalization
equalized_image = cv2.equalizeHist(image)

# Step 2: Canny Edge Detection
# Apply Canny edge detector
edges = cv2.Canny(equalized_image, 100, 200)

# Step 3: Hough Line Transformation
# Use HoughLinesP to detect lines in the edge image
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

# Draw the detected lines on a copy of the original image
line_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Plotting the results
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')

plt.subplot(2, 2, 3)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')

plt.subplot(2, 2, 4)
plt.title('Hough Line Detection')
plt.imshow(line_image)

plt.show()
