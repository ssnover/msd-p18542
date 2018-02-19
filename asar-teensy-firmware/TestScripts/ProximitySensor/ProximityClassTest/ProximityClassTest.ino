/*
 * ProximityClassTest.ino
 * Autho: Aaron Mallabar
 * Date: February 19, 2018
 * Description Testing the Proximity_Sensor Class
 */
#include "Proximity_Sensor.h"
#include "PITimer.h"

const int LED = 13;
const int Period = .1;
bool Flag = 0;

void callback();

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
  if (distance < 10)
  {
    digitalWrite(LED, HIGH);
  }
  else 
  {
    digitalWrite(LED, LOW);
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
