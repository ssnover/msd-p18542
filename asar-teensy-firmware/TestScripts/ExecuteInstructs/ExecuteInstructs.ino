/*
 * ExecuteInstructs.ino
 * Author: Aaron Mallabar
 * Date: March 9, 2018
 * Description: This Script takes in a set of instructions from the xbee.
 *              And executes the instructions using the the encoder. 
 *              (Set of five instructs)
 */
#include "Arduino.h"
#include "Motor.h"
#include "XBEE.h"
#include "PITimer.h"

const int LED = 13;
const double Period = .01;
bool Flag = false;
bool instructDone = false;
int CurrentInstruct = 1;
double disp = 0;
double angle = 0;
const int TURN_SPEED = 50;

void callback();
void executeCurrentInstruct();
void printStatus();

ASAR::XBEE myXBEE;
ASAR::MOTOR myMOTOR;

void setup() 
{
  Serial.begin(115200);
  delay(1000);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);
  myMOTOR.initEncoder();
  Serial.println("Waiting...");
  while(myXBEE.action[1] == 0)
  {
    myXBEE.getInstructions();
  }
  Serial.println("My Actions Are..");
  for(int i = 1; i < myXBEE.instructTotal; i++)
  {
    Serial.print(i); Serial.print(". ");
    Serial.println(myXBEE.action[i], HEX);
  }
  
}

void loop()
{
  while(Flag)
  {
    Flag = false;
    instructDone = false;
    disp = myMOTOR.getPosition(); //Initialize the displacement
    angle = myMOTOR.getAngle();   //Initializes the angle
    executeCurrentInstruct();
    if(instructDone)
    {
      printStatus();
      CurrentInstruct++;
      myMOTOR.initEncoder();
      digitalWrite(LED, !digitalRead(LED));
    }
  }
}

/*Used to start the main loop through timer interrupt*/
void callback()
{
  Flag = true;
}

/*Sends the current instruction to the motors*/
void executeCurrentInstruct()
{
  switch (myXBEE.action[CurrentInstruct])
  {
    case 0xAA : //Turn Left
      myMOTOR.LeftTurn(TURN_SPEED);
      if (angle <= -myXBEE.angle[CurrentInstruct])
      {
        instructDone = true;
      }
      break;
    case 0xBB : //Turn Right
      myMOTOR.RightTurn(TURN_SPEED);
      if (angle >= myXBEE.angle[CurrentInstruct])
      {
        instructDone = true;
      }
      break;            
    case 0xCC : //Go Forward
      myMOTOR.Forward(myXBEE.speedy[CurrentInstruct]);
      if (disp >= (myXBEE.distance[CurrentInstruct]))
      {
        instructDone = true;
      }
      break;  
    case 0x00 : //if No more instructions
      myMOTOR.Stop();
      Serial.println("All Done");      
      while(1)
      {
        //spin forever
      }
    default: //If the action type is not recognized
      myMOTOR.Stop();
      break;  
  }
}


void printStatus()
{
  Serial.print("Instruction: #"); Serial.println(CurrentInstruct);
  Serial.print("Displacement: "); Serial.print(disp); Serial.println(" cm");
  Serial.print("Angle: "); Serial.print(angle); Serial.println (" deg");
  Serial.println(myXBEE.action[CurrentInstruct], HEX);
}

