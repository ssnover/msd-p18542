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
 float angle = 0;

 const float goThisFar = 3;
 

void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  myMOTOR.initEncoder();

}
void loop()
{
//  myMOTOR.Forward(3);
//  delay(2000);
//  myMOTOR.Stop();
//  delay(1000);
//  myMOTOR.Backwards(3);
//  delay(2000);
//  myMOTOR.Stop();
//  delay(1000);
  distance = myMOTOR.getPosition();
  angle = myMOTOR.getAngle();
  Serial.print("Distance: "); Serial.print(distance);Serial.println(" Meters"); 
  Serial.print("Angle: "); Serial.print(angle);Serial.println(" Degrees"); 
  if (distance <= goThisFar && distance >= 0)
  {
    myMOTOR.Forward(3);
  }
  else if (angle <= 90)
  {
    myMOTOR.RightTurn(3);
  }
  else
  {
    myMOTOR.Stop();
  }

  delay(100);



}


  

  

