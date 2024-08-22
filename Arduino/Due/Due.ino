/*
 Mouse Controller Example

 Shows the output of a USB Mouse connected to
 the Native USB port on an Arduino Due Board.

 created 8 Oct 2012
 by Cristian Maglie

 http://www.arduino.cc/en/Tutorial/MouseController

 This sample code is part of the public domain.
 */

// Require mouse control library
#include <MouseController.h>

// Initialize USB Controller
USBHost usb;

// Attach mouse controller to USB
MouseController mouse(usb);

// variables for mouse button states
boolean leftButton = false;
boolean middleButton = false;
boolean rightButton = false;



// This function intercepts mouse button press
void mousePressed() {
  if (mouse.getButton(LEFT_BUTTON)) {
    Serial.println("L1");
    leftButton = true;
    return;
  }
  else if (mouse.getButton(MIDDLE_BUTTON)) {
    //Serial.print("M");
    //middleButton = true;
    //return
  }
  else if (mouse.getButton(RIGHT_BUTTON)) {
    Serial.println("R1");
    rightButton = true;
    return;
  }
}

// This function intercepts mouse button release
void mouseReleased() {
  if (!mouse.getButton(LEFT_BUTTON) && leftButton == true) {
    Serial.println("L0");
    leftButton = false;
    return;
  }
  if (!mouse.getButton(MIDDLE_BUTTON) && middleButton == true) {
    //Serial.print("M");
    //middleButton = false;
    //return;
  }
  if (!mouse.getButton(RIGHT_BUTTON) && rightButton == true) {
    Serial.println("R0");
    rightButton = false;
    return;
  }
}

void setup() {
  Serial.begin(115200);

  delay(200);
}

void loop() {
  // Process USB tasks
  usb.Task();
  int x=mouse.getXChange();
  int y=mouse.getYChange();
  if (x+y!=0)
  {
    Serial.println("M"+String(x)+" "+String(y)+" 0");
  }
  //if (mouse.getButton(LEFT_BUTTON)!=leftButton)
    //leftButton=!leftButton;
    //Serial.println("L"+String(leftButton));
}

