/*
 * XBEEClassTest.ino
 * Autho: Aaron Mallabar
 * Date: March 6, 2018
 * Description: Test the class i worte for xbee communication, should read instructions, and interpret it
 */
#include "XBEE.h"
#include "PITimer.h"

const int LED = 13;
const int Period = .1;
bool Flag = 0;

void callback();

ASAR::XBEE myXBEE;

void setup() 
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);

}

void loop()
{
  while(Flag)
  {
    Flag = false;
    myXBEE.GetInstructions(5);
  }
}

void callback()
{
    if (!Flag)
    {
      Serial.println("Error: Didn't Get to Bottom of Loop");
    }
  //digitalWrite(LED, !digitalRead(LED));
  Flag = true;
}
