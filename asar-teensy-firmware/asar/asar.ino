/*
 * file: asar.ino
 * purpose: Entry point for the execution of ASAR robot firmware.
 */


#include "Arduino.h"
#include "Execute.h"
#include "PITimer.h"

using namespace ASAR;

const double Period = .01;
bool Flag = false;
const int BAUD_RATE = 115200;

void callback();

EXECUTE myASAR;



void setup()
{

	// Initialization of drivers
  Serial.begin(BAUD_RATE);
  Serial1.begin(BAUD_RATE);
  delay(500);
  PITimer1.period(Period);
  PITimer1.start(callback);
  
}

/*Used to start the main loop through timer interrupt*/
void callback()
{
  Flag = true;
}


void loop()
{
		while (Flag)
    {
      myASAR.execute();
    }
}
