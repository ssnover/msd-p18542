/*
 * ExecuteInstructs.ino
 * Author: Aaron Mallabar
 * Date: March 9, 2018
 * Description: This Script takes in a set of instructions from the xbee.
 *              And executes the instructions using the the encoder. 
 *              (Set of five instructs)
 *              Forward Instruct: cc-distance-speed 
 *              LEFT = AA Right = BB
 *              
 *          
 */
 
#include "Arduino.h"
#include "Motor.h"
#include "XBEE.h"
#include "PITimer.h"

using namespace ASAR;

const int LED = 13;
const double Period = .01;
bool Flag = false;
bool instructDone = true;
bool printedReady = false;
bool readyForNew = true;
int CurrentInstruct = 1;
double displacement = 0;
double angle = 0;
const int TURN_SPEED = 240;

void callback();
void executeCurrentInstruct();
void printStatus(int serialPort);

ASAR::XBEE myXBEE;
ASAR::MOTOR myMOTOR;

void setup() 
{
  Serial.begin(115200);
  Serial1.begin(115200);
  delay(500);
  pinMode(LED, OUTPUT);
  PITimer1.period(Period);
  PITimer1.start(callback);
  myMOTOR.initEncoder();
  myXBEE.initInstruction();  
  delay(500);

}

void loop()
{
  if(Flag)
  {
    Flag = false;
    if (Serial1.available() > 0 && readyForNew)  //New Instructions might be available
    {
      if (myXBEE.getInstructions()) //If new instruction
      {
        myMOTOR.initEncoder();
        Serial.println("To Do list:");
        for(int i = 1; i <= myXBEE.instructTotal; i++)
        {
         Serial.print(i); Serial.print(". ");
         Serial.println(myXBEE.action[i], HEX);
        }
      }
    }
    else
    {
      if (myXBEE.action[1] == 0 && !printedReady)
      {
        Serial.println("Ready to Receive Instructions..."); 
        printedReady = true;
      }
      else if (myXBEE.action[1] == 0 && printedReady)
      { 
        //Do nothing
      }
      else //myXBEE.action[1] !=0;
      {
        //Serial.print("Here");
        instructDone = false;
        displacement = myMOTOR.getPosition(); //Initialize the displacement
        angle = myMOTOR.getAngle();   //Initializes the angle
        executeCurrentInstruct();
        if(instructDone)
        {
          Serial.println("Instruct Done");
          printStatus(0);
          CurrentInstruct++;
          printedReady = false;
          myMOTOR.initEncoder();
          digitalWrite(LED, !digitalRead(LED));
          myMOTOR.Stop();
          delay(250);
          Serial.print("Number of Instructions: "); Serial.println(myXBEE.instructTotal);
          Serial.print("Current Instruction: "); Serial.println(CurrentInstruct);
          if (myXBEE.instructTotal < CurrentInstruct)
          {
            myXBEE.initInstruction();
            CurrentInstruct = 1;
            instructDone = false;
            readyForNew = true;
          }
        }
      }
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
  switch (static_cast<XBEE::INSTRUCT_BYTE>(myXBEE.action[CurrentInstruct]))
  {
    case XBEE::INSTRUCT_BYTE::ACTION_LEFT: //Turn Left
      myMOTOR.LeftTurn(TURN_SPEED);
      if (angle <= -myXBEE.angle[CurrentInstruct])
      {
        instructDone = true;
      }
      break;
    case XBEE::INSTRUCT_BYTE::ACTION_RIGHT: //Turn Right
      myMOTOR.RightTurn(TURN_SPEED);
      if (angle >= myXBEE.angle[CurrentInstruct])
      {
        instructDone = true;
      }
      break;            
    case XBEE::INSTRUCT_BYTE::ACTION_FORWARD: //Go Forward
      myMOTOR.Forward(myXBEE.speedy[CurrentInstruct]);
      if (displacement >= (myXBEE.distance[CurrentInstruct]))
      {
        instructDone = true;
      }
      break;  
    case XBEE::INSTRUCT_BYTE::DONE_EXECUTION: //if No more instructions
      myMOTOR.Stop(); 
    default: //If the action type is not recognized
      myMOTOR.Stop();
      break;  
  }
}


void printStatus(int serialPort)
{
  if (serialPort == 0)
  {
    Serial.print("Instruction: #"); Serial.println(CurrentInstruct);
    Serial.print("Displacement: "); Serial.print(displacement); Serial.println(" cm");
    Serial.print("Angle: "); Serial.print(angle); Serial.println (" deg");
    //Serial.println(myXBEE.action[CurrentInstruct], HEX);
  }
  else
  {
    Serial.println("Sent things to the XBEE");
    Serial1.print("Instruction: #"); 
    Serial1.println(CurrentInstruct);
    Serial1.print("Displacement: "); Serial1.print(displacement);Serial1.println(" cm");
    Serial1.print("Angle: ");  Serial1.print(angle);Serial1.println (" deg");
    //Serial1.println(myXBEE.action[CurrentInstruct], HEX);
  }
}

