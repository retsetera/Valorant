from pynput import mouse
from pynput.mouse import Controller, Button
from Arduino.arduinomouse import ArduinoMouse, arduino_task

class Mouse:
    def __init__(self,use_arduino:bool):
            self.use_arduino = use_arduino
            if use_arduino:
                self.arduino_leo=ArduinoMouse('Leo')
                self.arduino_due=ArduinoMouse('Due')
            else:
                self.mouse = Controller()

    def mouse_task(self):
        if(self.use_arduino):
             arduino_task(self.arduino_leo,self.arduino_due)


    def move(self,x,y,wheel):
        if(self.use_arduino):
            self.arduino_leo.move(x,y,wheel)
        else:
            self.mouse.move(x,y)
    def go_to_point(self,point):
        if not self.use_arduino:
            self.mouse.position=point

    def click(self):
        if(self.use_arduino):
            self.arduino_leo.Click()
        else:
            self.mouse.click(Button.left)

    
    
                