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

 const float goThisFar = 3;
 

void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  myMOTOR.initEncoder();

}
void loop()
{
  distance = myMOTOR.getPosition();
  Serial.print("Distance: "); Serial.print(distance);Serial.println(" Meters"); 
  if (distance <= goThisFar)
  {
    myMOTOR.Forward(3);
  }
  else
  {
    myMOTOR.Stop();
  }

  delay(100);



}


  

  

