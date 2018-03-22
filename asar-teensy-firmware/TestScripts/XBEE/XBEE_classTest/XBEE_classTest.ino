/*
 * XBEEClassTest.ino
 * Autho: Aaron Mallabar
 * Date: March 6, 2018
 * Description: Test the class i worte for xbee communication, should read instructions, and interpret it
 */
#include "XBEE.h"
#include "PITimer.h"

const int LED = 13;
const double Period = .01;
bool Flag = 0;

void callback();

ASAR::XBEE myXBEE;

void setup() 
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);
  /*This section is trying to be used in Executeinstructs, and does not work*/
//  while(myXBEE.action[1] == 0)
//  {
//    myXBEE.GetInstructions(5);
//  }


  
}


void loop()
{
  while(Flag)
  {
    Flag = false;
    digitalWrite(LED, !digitalRead(LED));
    while(myXBEE.action[1] == 0)
    {
      myXBEE.getInstructions(5);
      if (myXBEE.action[1] != 0)
      {
        Serial.print("MyAction: ");Serial.println(myXBEE.action[1], HEX);
      }
    }
   // myXBEE.GetInstructions(5);
  }
}

void callback()
{
  Flag = true;
}
