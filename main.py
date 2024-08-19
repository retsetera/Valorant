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

activation_key='l'


#setup
arduino_leo = ArduinoMouse('Leonardo')
#arduino_due = ArduinoMouse('Due')
camera = dxcam.create(output_color='BGR')
mouse = Controller()
screen = camera.grab()
#screen = cv2.resize(screen, (0,0), fx=2/3, fy=2/3)
resolution=(screen.shape[0], screen.shape[1])
#middle_of_screen = (math.floor(resolution[0]/2), math.floor(resolution[1]/2))
middle_of_screen=(camera.region[2]/2,camera.region[3]/2)

true_middle=(camera.region[2]/2,camera.region[3]/2)

screen = None

current_mouse_state=[] #x, y, wheel, left, right


while True:
    """serial_read = arduino_due.read_serial()
    if serial_read is not None:
        new_mouse = map(int, serial_read.split())
        arduino_leo.input(new_mouse)"""
        
    if not keyboard.is_pressed(activation_key):
        continue
    img = camera.grab()
    if img is not None:
        screen=img
    #screen = cv2.resize(screen, (0,0), fx=0.4, fy=1.2)

    data, picture = outline_filter(screen,0)
    contours = [x[0] for x in data]
    positions = [x[1] for x in data]
    if len(contours)==0:
        continue
    biggest_contour=cv2.contourArea(contours[0])
    biggest_contour_index = 0
    for i in range(len(contours)-1):
        if cv2.contourArea(contours[i+1])>biggest_contour:
            biggest_contour_index=i+1
            biggest_contour = cv2.contourArea(contours[biggest_contour_index])
    
    position = positions[biggest_contour_index]

    position=(math.floor((position[0]-middle_of_screen[0])*2/3)+middle_of_screen[0],math.floor((position[1]-middle_of_screen[1])*2/3)+middle_of_screen[1])

    mpvariation = math.floor(math.dist(middle_of_screen, position)/2)
    curve = get_curve(middle_of_screen, position, mpvariation, sigmoid_time_func, middle_of_screen)

    mouse.position=true_middle
    for point in curve:
        if (not keyboard.is_pressed(activation_key)):
            break
        #mouse.position = (mouse.position[0]+point[0], mouse.position[1]+point[1])
        arduino_leo.move(point[0],point[1],0)

    if (keyboard.is_pressed(activation_key)):
        #arduino_leo.Click()
        print()



    """for point in curve:
        arduino.move(arduino, x=point[0], y=point[1])

    arduino.click(arduino)"""



