import numpy as np
from PIL import Image
from copy import deepcopy
import cv2
import os
import math

def outline_filter(_img,color):
    img=np.asarray(_img)
    colors = np.array([[[135, 35, 20],[155, 255, 255]],[[144, 75, 20],[158, 255, 255]]],dtype='uint8')#purple,
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, colors[color][0], colors[color][1])

    dilated = cv2.dilate(mask, None, iterations=5)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = contours
    if not contours:
        return
    contours = [i for i in contours if cv2.contourArea(i)>=1000]

    positions=[]
    onblank = np.zeros(hsv.shape, dtype='uint8')
    onblank = cv2.drawContours(onblank, contours, -1, (0, 255, 0), 1, cv2.LINE_AA)
    
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        
        amount_to_shift = (math.floor(0.45*w),math.floor(0.1*h))
        onblank = cv2.rectangle(onblank, (x,y),(x+w,y+h), (0,255,0),2)
        onblank = cv2.circle(onblank, (x+amount_to_shift[0], y+amount_to_shift[1]), radius=0, color=(0,255,0), thickness=2)
        positions.append([contour, (x+amount_to_shift[0], y+amount_to_shift[1])])
    return positions, onblank

#new = outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-1024x576.jpg"), 0)
#print()


