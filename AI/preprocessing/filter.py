import numpy as np
from PIL import Image
from copy import deepcopy
import cv2
import os

def outline_filter(_img,color):
    img=np.asarray(_img)
    colors = [[[135, 35, 20],[155, 255, 255]]]#purple,
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, np.array(colors[color][0], dtype='uint8'), np.array(colors[color][1], dtype='uint8'))
    
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(mask, kernel, iterations=4)
    ret, thresh = cv2.threshold(dilated, 40, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    onblank = np.zeros(hsv.shape, dtype='uint8')
    onblank = cv2.drawContours(onblank, contours, -1, (0, 255, 0), 1, cv2.LINE_AA)

    return Image.fromarray(onblank)

def outline_filter_dataset(datset_location, color):
    locations=['/test/images/', '/train/images/', '/valid/images/']
    for location in locations:
        for dir in os.listdir(datset_location+location):
            path = datset_location+location+dir
            img = Image.open(path)
            newimg = outline_filter(img, 0)
            os.remove(path)
            cv2.imwrite(path, np.asarray(newimg))

new = outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-1024x576.jpg"), 0)
print()


