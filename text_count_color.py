import cv2
import numpy as np

img = cv2.imread('Untitled.png')
img = cv2.medianBlur(img, ksize= 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[: 2]

def solve(thresh, blank):
    global width
    ans = 0
    track = 0
    for i in range(width):
        val = np.sum(img[:, i])
        if val <= thresh:
            track += 1
        else:
            if track >= blank:
                ans += 1
            track = 0
    return ans + 1

print(solve(50, 3))