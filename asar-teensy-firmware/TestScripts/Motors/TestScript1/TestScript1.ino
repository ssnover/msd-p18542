/* TestScript1.ino
 *  Author: Aaron Mallabar
 *  Date:   January 18,2017
 *  Description: Start Testing some of the capabilities of our MSD prototype Robot PCB.
 *  1. Motor Movement
 *  
 */

 #include "MOTOR.h"

 ASAR::MOTOR myMOTOR;

 float distance = 0;
 

void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);

}
void loop()
{
  Serial.println("Go");
  myMOTOR.getPosition();
  distance = myMOTOR.Robot_position;
  Serial.print("Distance: "); Serial.print(distance);Serial.println(" Meters"); 
  digitalWrite(13, !digitalRead(13));
  delay(500);
  

}


  

  

