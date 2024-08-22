import numpy as np
import dxcam
from preprocessing.filter import outline_filter
from MathFunctions.curve import get_curve, sigmoid_time_func
from Arduino.arduinomouse import ArduinoMouse
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


class dan_no_arduino:
    
    def __init__(self, resolution, activation_key='caps lock', color=0):
        self.activation_key=activation_key
        self.color=color


        self.camera = ScreenCapture(0,0,resolution)
        self.resolution=resolution
        self.middle_of_screen=(resolution[0]/2,resolution[1]/2)
        self.mouse=Controller()



    def task(self):
        if not keyboard.is_pressed(self.activation_key):

            #arduino_task(self.arduino_leo, self.arduino_due)
            return
            
        
        img = self.camera.get_screen()
        if img is not None:
            screen=img

        data, picture = outline_filter(screen,self.color)
        
        contours = [x[0] for x in data]
        positions = [x[1] for x in data]
        if len(contours)==0:
            return
        min_dist=math.dist(self.middle_of_screen,positions[0])
        min_dist_index=0
        for i in range(1,len(positions)):
            if math.dist(self.middle_of_screen,positions[i])<min_dist:
                min_dist_index=i
                min_dist= math.dist(self.middle_of_screen,positions[i])
        position = positions[min_dist_index]


        mpvariation = math.floor(min_dist/2)
        curve = get_curve(self.middle_of_screen, position, mpvariation, sigmoid_time_func, self.middle_of_screen)

        self.mouse.position=self.middle_of_screen
        amount_to_delay=0.0005*min_dist
        for point in curve:
            if (not keyboard.is_pressed(self.activation_key)):
                break
            self.mouse.position = (self.mouse.position[0]+point[0], self.mouse.position[1]+point[1])
            #time.sleep()

        if (keyboard.is_pressed(self.activation_key)):
            self.mouse.click(Button.left)
            

        """for point in curve:
            arduino.move(arduino, x=point[0], y=point[1])

        arduino.click(arduino)"""






bot = dan_no_arduino((1920,1080),color=0,activation_key='ctrl')
while True:
    bot.task()
