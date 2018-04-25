/* TestScript1.ino
 *  Author: Aaron Mallabar
 *  Date:   January 18,2017
 *  Description: Start Testing some of the capabilities of our MSD prototype Robot PCB.
 *  1. Motor Movement
 *  
 */

#include "Motor.h"
#include "Proximity_Sensor.h"
#include "PITimer.h"

const int LED = 13;
const int Period = .1;
const int OBSTACLE_THRESHOLD = 25;
const int MOTOR_SPEED = 150;
const int DELAY_TIME = 50;
bool Flag = 0;

void callback();

ASAR::MOTOR myMOTOR;
ASAR::Proximity_Sensor myPing;

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
  if (distance < OBSTACLE_THRESHOLD)
  {
    digitalWrite(LED, HIGH);
    myMOTOR.Forward(MOTOR_SPEED);
    
  }
  else 
  {
    digitalWrite(LED, LOW);
    myMOTOR.Stop();
    delay(DELAY_TIME);
    myMOTOR.Backwards(MOTOR_SPEED);
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

  

  

