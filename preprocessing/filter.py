import numpy as np
from PIL import Image
from copy import deepcopy
import cv2
import os
import math
from pathlib import Path

reference_contour=np.load((Path(__file__) / '../ContourReferences/reference_contour1.npy').resolve())
def outline_filter(_img,color):
    img=np.asarray(_img)
    #kinda works, mine,
    colors = np.array([[[135, 35, 60],[155, 255, 255]],[[135, 35, 65],[155, 255, 255]]],dtype='uint8')#purple,
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, colors[color][0], colors[color][1])

    dilated = cv2.dilate(mask, None, iterations=5)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contours)==0:
        return [],deepcopy(img)

    #contours = [i for i in contours if (cv2.contourArea(i)>=2000)]
    contours = [i for i in contours if (cv2.contourArea(i)>=2000) and (cv2.matchShapes(i,reference_contour,1,0.0)<0.5)]
    if len(contours)==0:
        return [],deepcopy(img)
    positions=[]
    #onblank = np.zeros(hsv.shape, dtype='uint8')
    onblank=deepcopy(img)
    onblank = cv2.drawContours(onblank, contours, -1, (0, 255, 0), 1, cv2.LINE_AA)
    
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        
        amount_to_shift = (math.floor(0.45*w),math.floor(0.1*h))
        onblank = cv2.rectangle(onblank, (x,y),(x+w,y+h), (0,255,0),2)
        onblank = cv2.circle(onblank, (x+amount_to_shift[0], y+amount_to_shift[1]), radius=0, color=(0,255,0), thickness=2)
        positions.append([contour, (x+amount_to_shift[0], y+amount_to_shift[1])])
    return positions, onblank

#new = outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-Enemy-VALORANT-1024x576.jpg"), 0)
#print()
