import cv2
import numpy as np
fl = cv2.IMREAD_GRAYSCALE
img = cv2.imread('img.png')
cv2.imshow("Image", img)
# # # kernel = np.array([[50,100,50],[200,500,200],[50,100,50]], dtype=np.uint8)
# # # edge = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel=kernel, iterations=1)
# # edge = cv2.Canny(img, 0, 255)
# # # print(img.dtype)
# # edge = cv2.Laplacian(src=img, ddepth=cv2.CV_64F ,ksize=11)
# # edge = 255-edge # Negative
# # edge = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=1)
# # cv2.imshow("Edge", edge)
# r1 = 70
# s1 = 0
# r2 = 140
# s2 = 255
# def pix(value, r1, s1, r2, s2):
#     if (0<=value and value<=r1):
#         return (s1/r1) * value
#     elif (r1<value and value <=r2):
#         return ((s2-s1)/(r2-r1)) * (value - r1) + s1
#     else :
#         return ((255-s2)/(255-r2)) * (value - r2) + s2
# pix_vec = np.vectorize(pix)
# contrast = pix_vec(img, r1, s1, r2, s2)
# cv2.imshow("Contrast Streched",contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()