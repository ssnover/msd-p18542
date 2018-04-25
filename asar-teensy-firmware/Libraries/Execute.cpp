#include "Arduino.h"
#include "Execute.h"


namespace ASAR
{
  EXECUTE::EXECUTE()
  {
    
    pinMode(LED, OUTPUT);
    myMOTOR.initEncoder();
    myXBEE.initInstruction(); 
  }
  
  EXECUTE::~EXECUTE()
  {
  	//Empty Destructor
  }
    
  void EXECUTE::execute()
  {
    if (Serial1.available() > 0 && readyForNew)  //New Instructions might be available
    {
      if (myXBEE.getInstructions()) //If new instruction
      {
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
        Serial1.println("Ready to Receive Instructions..."); 
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
          Serial1.println("Instruct Done");
          printStatus(1);
          CurrentInstruct++;
          printedReady = false;
          myMOTOR.initEncoder();
          digitalWrite(LED, !digitalRead(LED));
          myMOTOR.Stop();
          delay(INSTRUCTION_2_INSTRUCTION_DELAY);
          myMOTOR.Speed = 0;
          Serial1.print("Number of Instructions: "); Serial1.println(myXBEE.instructTotal);
          Serial1.print("Current Instruction: "); Serial1.println(CurrentInstruct);
          readyForNew = true;
          if (myXBEE.instructTotal < CurrentInstruct)
          {
            myXBEE.initInstruction();
            CurrentInstruct = 1;
            instructDone = false;
          }
        }
      }
    }
  }

  /*Sends the current instruction to the motors*/
  void EXECUTE::executeCurrentInstruct()
  {
    switch (static_cast<XBEE::INSTRUCT_BYTE>(myXBEE.action[CurrentInstruct]))
    {
      case XBEE::INSTRUCT_BYTE::ACTION_LEFT: //Turn Left
        myMOTOR.LeftTurn(TURN_SPEED);
        if (angle >= myXBEE.angle[CurrentInstruct])
        {
          instructDone = true;
        }
        break;
      case XBEE::INSTRUCT_BYTE::ACTION_RIGHT: //Turn Right
        myMOTOR.RightTurn(TURN_SPEED);
        if (angle <= -myXBEE.angle[CurrentInstruct])
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
      case XBEE::INSTRUCT_BYTE::ACTION_STAHP:
        Serial1.println("STOPPING!!!");
        myMOTOR.Stop();
        myXBEE.initInstruction();
        instructDone = true;
        break;
      case XBEE::INSTRUCT_BYTE::DONE_EXECUTION: //if No more instructions
        myMOTOR.Stop(); 
      default: //If the action type is not recognized
        myMOTOR.Stop();
        break;  
    }
  }

  void EXECUTE::printStatus(int serialPort)
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
} // namespace ASAR
