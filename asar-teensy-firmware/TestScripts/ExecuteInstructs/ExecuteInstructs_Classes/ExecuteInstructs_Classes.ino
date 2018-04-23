/*
 * Execute.ino
 * Author: Aaron Mallabar
 * Date: March 20, 2018
 * Description: Tests the EXECUTE CLass
 *              
 *          
 */
#include "Arduino.h"
#include "Execute.h"
#include "PITimer.h"

using namespace ASAR;

const double Period = .01;
bool Flag = false;

void callback();

EXECUTE myASAR;



void setup() 
{
  Serial.begin(115200);
  Serial1.begin(115200);
  delay(500);
  PITimer1.period(Period);
  PITimer1.start(callback);
}

void loop() 
{
  while (Flag)
  {
    myASAR.execute();
  }
}

/*Used to start the main loop through timer interrupt*/
void callback()
{
  Flag = true;
}
