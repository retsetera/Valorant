import numpy as np
from PIL import Image
from copy import deepcopy
import cv2
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt
reference_contour=np.load((Path(__file__) / '../ContourReferences/reference_contour1.npy').resolve())
reference_contour2=np.load((Path(__file__) / '../ContourReferences/reference_contour2.npy').resolve())
def outline_filter(_img,color,fov):
    img=np.asarray(_img)
    center_of_screen = (int(img.shape[1]/2),int(img.shape[0]/2))
    #kinda works, mine,
    colors = np.array([[[135, 35, 60],[155, 255, 255]],[[135, 35, 65],[155, 255, 255]]],dtype='uint8')#purple,
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, colors[color][0], colors[color][1])

    dilated = cv2.dilate(mask, None, iterations=3)#iteration needs to be twea
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contours)==0:
        return [],deepcopy(img)

    contours = [i for i in contours if ((cv2.contourArea(i)>=1500))]
    
    #contours = [i for i in contours if (cv2.contourArea(i)>=1500) and ((cv2.matchShapes(i,reference_contour,1,0.0)<0.2) or (cv2.matchShapes(i,reference_contour2,1,0.0)<0.3))]
    if len(contours)==0:
        return [],deepcopy(img)
    positions=[]
    #onblank = np.zeros(hsv.shape, dtype='uint8')
    onblank=deepcopy(img)
    onblank = cv2.drawContours(onblank, contours, -1, (0, 255, 0), 1, cv2.LINE_AA)
    onblank = cv2.circle(onblank,center_of_screen,fov,(0,0,255),2)
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        
        amount_to_shift = (math.floor(0.5*w),math.floor(0.1*h))
        onblank = cv2.rectangle(onblank, (x,y),(x+w,y+h), (0,255,0),2)
        onblank = cv2.circle(onblank, (x+amount_to_shift[0], y+amount_to_shift[1]), radius=0, color=(0,255,0), thickness=2)
        position = (x+amount_to_shift[0], y+amount_to_shift[1])
        if math.dist(position, center_of_screen)<=fov:
            positions.append([contour, position])
    return positions, onblank

def check_area(position):
    return cv2.contourArea(position[0])

#data,picture=outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-1024x576.jpg"),0,300)
