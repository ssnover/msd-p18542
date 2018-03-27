/*
 * XBEEClassTest.ino
 * Autho: Aaron Mallabar
 * Date: March 6, 2018
 * Description: Test the class i worte for xbee communication, should read instructions, and interpret it
 */
#include "XBEE.h"
#include "PITimer.h"

const int LED = 13;
const double Period = .1;
bool Flag = 0;

void callback();

ASAR::XBEE myXBEE;

void setup() 
{
  Serial.begin(9600);
  delay(1000);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);
  /*This section is trying to be used in Executeinstructs, and does not work*/
  Serial.println("Waiting for initial Set of Instructions");
  while(myXBEE.action[1] == 0)
  { 
    myXBEE.getInstructions();
  }
}


void loop()
{
  while(Flag)
  {
    Flag = false;
    Serial.println("Waiting for instructions");
    myXBEE.getInstructions();
  }
}

void callback()
{
  Flag = true;
  digitalWrite(LED, !digitalRead(LED));
}
