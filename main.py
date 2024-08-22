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


class dan:
    
    def __init__(self, resolution, activation_key='caps lock', color=0):
        self.activation_key=activation_key
        self.color=color
        #setup
        self.arduino_leo = ArduinoMouse('Leonardo')
        self.arduino_due = ArduinoMouse('Due')

        #camera = dxcam.create(output_color='BGR')
        self.camera = ScreenCapture(0,0,resolution)
        #screen = cv2.resize(screen, (0,0), fx=2/3, fy=2/3)
        self.resolution=resolution
        #middle_of_screen = (math.floor(resolution[0]/2), math.floor(resolution[1]/2))
        self.middle_of_screen=(resolution[0]/2,resolution[1]/2)



    def task(self):
        if not keyboard.is_pressed(self.activation_key):

            arduino_task(self.arduino_leo, self.arduino_due)
            return
            
        
        print('6') 
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

        position=(math.floor((position[0]-self.middle_of_screen[0])*3.7)+self.middle_of_screen[0],math.floor((position[1]-self.middle_of_screen[1])*3.7)+self.middle_of_screen[1])

        mpvariation = math.floor(min_dist/2)
        curve = get_curve(self.middle_of_screen, position, mpvariation, sigmoid_time_func, self.middle_of_screen)

        #mouse.position=true_middle
        amount_to_delay=0.0005*min_dist
        for point in curve:
            if (not keyboard.is_pressed(self.activation_key)):
                break
            #mouse.position = (mouse.position[0]+point[0], mouse.position[1]+point[1])
            self.arduino_leo.move(point[0],point[1],0)
            time.sleep()

        if (keyboard.is_pressed(self.activation_key)):
            self.arduino_leo.Click()


        """for point in curve:
            arduino.move(arduino, x=point[0], y=point[1])

        arduino.click(arduino)"""


bot = dan((1920,1080),'ctrl',0)
while True:
    bot.task()

