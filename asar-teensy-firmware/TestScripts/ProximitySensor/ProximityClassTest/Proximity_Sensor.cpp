/* Proximity_Sensor.cpp
 *  Author: Aaron Mallabar
 *  Date:   February 19, 2018
 	Last Update: February 19, 2018
 *  Description: Low Level Motor Control
 *  
 */
 

#include "Arduino.h"
#include "Proximity_Sensor.h"


namespace ASAR
{
Proximity_Sensor::Proximity_Sensor()
{
	pinMode(this->trigPin, OUTPUT);
	pinMode(this->echoPin, INPUT);
}

Proximity_Sensor::~Proximity_Sensor()
{
	//Empty Destructor
}




int Proximity_Sensor::CheckProximity()
{
  int duration = 0;  //Time taken to receive signal back (proportional to distance)
  double distance = 0; //Distance away from an object

 /*
  * Sends out a pulse
  */
  digitalWrite(trigPin, LOW);  
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH); //waits to receive pulse, and times it
  distance = duration*0.034/2; //convert to a distance, (possibly cm?)
  return distance;
}
}//NameSpace ASAR