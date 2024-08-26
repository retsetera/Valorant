import numpy as np
import dxcam
from preprocessing.filter import outline_filter
from MathFunctions.curve import get_curve, sigmoid_time_func
from Arduino.arduinomouse import ArduinoMouse, arduino_task
import cv2
import pyautogui
import keyboard
import math
from pynput import mouse
from pynput.mouse import Controller, Button
import time
from PIL import Image
from screen_cap import ScreenCapture
import matplotlib.pyplot as plt
from Mouse.MouseHandler import Mouse
from preprocessing.filter import check_area


class dan:
    
    def __init__(self, resolution, fov,activation_key='caps lock', color=0,use_arduino=False,vdpi=1):
        self.activation_key=activation_key
        self.color=color
        self.fov=fov
        self.vdpi=1/vdpi
        self.resolution=resolution


        self.camera = ScreenCapture(0,0,resolution)
        self.middle_of_screen=(resolution[0]/2,resolution[1]/2)
        self.mouse=Mouse(use_arduino)
    def task(self):
        if not keyboard.is_pressed(self.activation_key):
            self.mouse.mouse_task()
            return
            
        
         
        img = self.camera.get_screen()
        if img is not None:
            screen=img
        data, picture = outline_filter(screen,self.color,self.fov)
        contours = [x[0] for x in data]
        positions = [x[1] for x in data]
        if len(contours)==0:
            self.mouse.mouse_task()
            return

        position = max(data,key=check_area)[1]
        dist = math.dist(position,self.middle_of_screen)
        
        position=(math.floor((position[0]-self.middle_of_screen[0])*self.vdpi)+self.middle_of_screen[0],math.floor((position[1]-self.middle_of_screen[1])*self.vdpi)+self.middle_of_screen[1])

        mpvariation = math.floor(dist*0.2)
        curve = get_curve(self.middle_of_screen, position, mpvariation, sigmoid_time_func, self.middle_of_screen)

        self.mouse.go_to_point(self.middle_of_screen)
        amount_to_delay=0.00000000001*dist
        for point in curve:
            if (not keyboard.is_pressed(self.activation_key)):
                break
            self.mouse.move(point[0],point[1],0)
            #time.sleep(amount_to_delay)

        

        if (keyboard.is_pressed(self.activation_key)):
            self.mouse.click()
        



bot = dan((2560,1080),500,'ctrl',0,True,3/2)
while True:
    bot.task()

