

#include <Mouse.h>
#include <Mouse.h>

float x_offset, y_offset;
void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(10);
  Mouse.begin();
}



void loop()
{
  if (Serial.available() > 0)
  {
    char inChar = Serial.read();
    if (inChar=='M')
    {
      signed char x = Serial.parseInt();
      signed char y = Serial.parseInt();
      signed char wheel = Serial.parseInt();
      
      Mouse.move(x, y, wheel);
    }
    else if (inChar=='L')
    {
      int status = Serial.parseInt();

      if (status==1) Mouse.press(MOUSE_LEFT);
      else Mouse.release(MOUSE_LEFT);
    }
    else if (inChar=='R')
    {
      int status = Serial.parseInt();

      if (status==1) Mouse.press(MOUSE_RIGHT);
      else Mouse.release(MOUSE_RIGHT);
    }
  }
}
