import cv2
import numpy as np 

def preprocess_img(image_path):
    img = cv2.imread(image_path)
    img = cv2.medianBlur(img,ksize=3)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray_img

def count_blank_regions(img,threshold,blank_length):
    height,width = img.shape
    word_count = 0
    consecutive_blank_cols = 0
    in_word = False

    for i in range(width):
        avg_pixel_value= np.mean (img[:,i])

    if avg_pixel_value > threshold:
        if not in_word:
            word_count += 1
            in_word = True
        consecutive_blank_cols = 0
    else:
        consecutive_blank_cols += 1
        if consecutive_blank_cols >= blank_length:
            in_word = False

    return word_count

if __name__ == "__main__":
    img = preprocess_img('text.png')
    result = count_blank_regions(img,threshold=50,blank_length=3)
    print("No. of words ",result) 