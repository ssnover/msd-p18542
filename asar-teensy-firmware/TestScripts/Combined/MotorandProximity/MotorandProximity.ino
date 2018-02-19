/* TestScript1.ino
 *  Author: Aaron Mallabar
 *  Date:   January 18,2017
 *  Description: Start Testing some of the capabilities of our MSD prototype Robot PCB.
 *  1. Motor Movement
 *  
 */

 #include "MOTOR.h"
 #include "Proximity_Sensor.h"
 #include "PITimer.h"

const int LED = 13;
const int Period = .1;
bool Flag = 0;

void callback();

 ASAR::MOTOR myMOTOR;
 ASAR::Proximity_Sensor myPing;

 void callback();

void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);
}

void loop()
{
  int distance = 0;
  distance = myPing.CheckProximity();
  Serial.println(distance);
  if (distance < 25)
  {
    digitalWrite(LED, HIGH);
    myMOTOR.Forward(5);
    
  }
  else 
  {
    digitalWrite(LED, LOW);
    myMOTOR.Stop();
    delay(5);
    myMOTOR.Backwards(5);
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

  

  

