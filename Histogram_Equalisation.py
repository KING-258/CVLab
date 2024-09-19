import cv2
import numpy as np
import matplotlib.pyplot as plt
def histogram_equalization(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    equalized_image = cv2.equalizeHist(image)
    cv2.imwrite(output_path, equalized_image)
    print(f"Equalized image saved at {output_path}")
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("Equalized Image")
    plt.imshow(equalized_image, cmap='gray')
    plt.show()
image_path = 'img.png'
output_path = '/home/professor_258/Documents/CVLab/out.png'
histogram_equalization(image_path, output_path)