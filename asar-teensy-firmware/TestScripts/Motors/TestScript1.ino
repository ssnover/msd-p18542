/* TestScript1.ino
 *  Author: Aaron Mallabar
 *  Date:   January 18,2017
 *  Description: Start Testing some of the capabilities of our MSD prototype Robot PCB.
 *  1. Motor Movement
 *  
 */

 #include "MOTOR.h"

 ASAR::MOTOR myMOTOR;
 

void setup()
{
  
}
void loop()
{
  myMOTOR.Forward(5);
  delay(2000);
  myMOTOR.Stop();
  delay(1000);
  myMOTOR.Forward(1);
  delay(2000);
  myMOTOR.Stop();
  delay(1000);
  myMOTOR.RightTurn(3);
  delay(2000);
  myMOTOR.Stop();
  delay(500);
  myMOTOR.LeftTurn(3);
  delay(2000);
  myMOTOR.Stop();
  delay(1000);
}


  

  

