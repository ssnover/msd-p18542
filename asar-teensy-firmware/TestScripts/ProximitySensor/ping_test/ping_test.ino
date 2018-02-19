/*
 * Author: Aaron Mallabar
 * Date: December 18, 2018
 * Description: Quick Test Script for the HCS-04 (ping) sensor
 *      Lights up an LED if an object is within 10 cm of the sensor
 */

#include "PITimer.h"

const int LEDpin = 13;  //LED Indicatior
const int trigPin = 21; //Sensor Transmitter
const int echoPin = 20; //Sensor Receiver
const double sPeriod = .1; //Period of Loop
double Time = 0; //Time since beginning of function
bool Flag = false; //loop starter flag
auto obstacleDist = 0; //Distance to nearest object

void callback(); //Interrupt to start loop
int CheckPing(); //Returns a distance from ping

void setup()
{
  Serial.begin(9600);  // Initialize Serial port
  Serial.println("Timer Begin");
  pinMode(LEDpin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  PITimer1.period(sPeriod);     // initialize timer1
  PITimer1.start(callback);     // attaches callback() as a timer overflow interrupt

}

void loop()
{

  while (Flag)   //Only starts once a period
  {
    Flag = false; //So that it wont start again until interrupt raises flag
    obstacleDist = CheckPing(); //Function call to check ping
    Serial.println(obstacleDist); //Pring the distance away from an object
   
    /*
     * If Something is close to the sensor, light up the led
     */
    if (obstacleDist <= 10)
    {
      digitalWrite(LEDpin, HIGH);
    }
    else 
    {
      digitalWrite(LEDpin, LOW);
    }
    
  }

}

void callback()
{
  //digitalWrite(LEDpin, digitalRead(13) ^ 1);
  Time = Time + sPeriod;
  Flag = true;
}

int CheckPing()
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

