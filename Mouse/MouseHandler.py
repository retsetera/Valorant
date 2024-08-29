from pynput import mouse
from pynput.mouse import Controller, Button
from Arduino.arduinomouse import ArduinoMouse, mouse_passthrough

class Mouse:
    def __init__(self,use_arduino:bool):
            self.use_arduino = use_arduino
            if use_arduino:
                self.arduino_leo=ArduinoMouse('Leo')
                self.arduino_due=ArduinoMouse('Due')
                self.mouse_passthrough = mouse_passthrough(self.arduino_leo, self.arduino_due)
            else:
                self.mouse = Controller()

    def get_leo(self):
        return self.arduino_leo
    
    def get_due(self):
        return self.arduino_due

    def mouse_passthrough(self,activated):
        if(self.use_arduino):
            self.mouse_passthrough.set_activated(activated)


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

    
    
                