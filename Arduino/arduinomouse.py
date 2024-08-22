import serial
from serial.tools import list_ports

import random
import time
import sys
from termcolor import colored



class ArduinoMouse:
    def __init__(self, port_search_term):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0.001
        self.serial_port.port = self.find_serial_port(port_search_term)
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[Error]', 'red'), colored('Program is already open or the serial port is being used by another app.', 'white'))
            sys.exit()

    def find_serial_port(self, port_search_term):
        port = next((port for port in list_ports.comports() if (("Arduino" in port.description) and (port_search_term in port.description))), None)
        if port is not None:
            return port.device
        else:
            print(colored('[Error]', 'red'), colored('No serial port found. Check your Arduino and try again.', 'white'))
            sys.exit()



    def move(self, x=0, y=0, wheel=0):
        #x = x + 256 if x < 0 else x
        #y = y + 256 if y < 0 else y
        self.serial_port.write(('M'+str(int(x))+' '+str(int(y))+' '+str(int(wheel))).encode())
        
    def Click(self):
        self.Left_Mouse(True)
        time.sleep(0.001)
        self.Left_Mouse(False)


    def Left_Mouse(self, status: bool=False):
        self.serial_port.write(('L'+str(int(status))).encode())
    def Right_Mouse(self, status: bool=False):
        self.serial_port.write(('R'+str(int(status))).encode())

    def read_serial(self):
        return self.serial_port.readline().decode()
    
    def write_serial(self,text):
        self.serial_port.write(text)

    def close(self):
        self.serial_port.close()

    def __del__(self):
        self.close()


