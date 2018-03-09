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
  
  distance = myMOTOR.getPosition();
  Serial.print("Distance: "); Serial.print(distance);Serial.println(" Meters"); 
  myMOTOR.initPosition();
  digitalWrite(13, !digitalRead(13));
  myMOTOR.Forward(1);
  delay(1200);
  myMOTOR.Stop();
  delay(500);
  
  
  
  

}


  

  

