/* XBEE.cpp
 *  Author: Aaron Mallabar
 *  Date:   March 6,2018
 *  Description: Header file that wraps us the serial commands to read info from the XBEE
 *				and interprets the information into executable directions
 *  
 */

#include "Arduino.h"
#include "XBEE.h"
#include "Wire.h"

namespace ASAR
{
	XBEE::XBEE()
	{
		Serial1.begin(BAUD_RATE);      	//Initialize Xbee, with baud rate
	}

	XBEE::~XBEE()
	{
		//empty destructor
	}

  /*Set Everything equal to zero*/
  void XBEE::initInstruction() 
  {
    Serial.println("Initializing...");
    for(int i=0; i <= 255; i++)
    {
      if (i <= 5)
      {
        singleRead[i] = 0x00;           //temporary hold place from direct reading of xbee
      }
      action[i] = 0x00;
      distance[i] = 0x00;
      angle[i] = 0x00;
      speedy[i] = 0x00;
      allRawPrevious[i] = allRaw[i];
      allRaw[i] = 0x00;
     }
      instructTotal = 1;          //total instructions
      instructNum = 1;            //couner for instruction number initialized to one
      rawReadIndex = 0;     
  }

  /*Read everything in buffer from XBEE, should be entire instruct set*/
  void XBEE::readAllRaw()
  {
    bool done_flag = false; //flag signaling Completely done with instruction set
    bool start_flag = false; //flag signaling that BYTEs are actuallaly part of instructuin
    int index = 0; //index that cycles through xbee buffer
    instructTotal = 0;
    while (!done_flag)
    { 
      if (Serial1.available())
      {
        allRaw[index] = Serial1.read();
        if (   index            >= 2 
            && INSTRUCT_BYTE::END_INSTRUCT_SET == static_cast<INSTRUCT_BYTE>(allRaw[index])
            && INSTRUCT_BYTE::END_INSTRUCT_SET == static_cast<INSTRUCT_BYTE>(allRaw[index - 1])
            && INSTRUCT_BYTE::END_INSTRUCT_SET == static_cast<INSTRUCT_BYTE>(allRaw[index - 2]))
        {
          done_flag = true;
          for (int i = 0; i <= 2; i++)
          {
            allRaw[index - i] = 0;
          }
         for (int i = 0; i <= index; i++)
          {
           //Serial.print(i); Serial.print(". "); Serial.println(allRaw[i], HEX);
          }
        }
        else if (INSTRUCT_BYTE::END_SINGLE_INSTRUCT == static_cast<INSTRUCT_BYTE>(allRaw[index]) && start_flag)
        {
          instructTotal++; 
          Serial.print("Instruct Total: "); Serial.println(instructTotal);
          start_flag = false;
        }
        else if (INSTRUCT_BYTE::START_INSTRUCT == static_cast<INSTRUCT_BYTE>(allRaw[index]))
        {
          start_flag = true;
        }
        index++;
      }
    }
    sameInstructFlag = true;
    for (int i = 0; i <= 1023; i++)
    {
      if(allRaw[i] != allRawPrevious[i])
      {
        //Serial.print(i); Serial.print(". "); Serial.print(allRaw[i]); Serial.print(" and "); Serial.println(allRawPrevious[i]);
        sameInstructFlag = false;
        Serial.println("NEW INSTRUCTIONS!");
        break;
      }
    }
    if (sameInstructFlag == true)
    {
      Serial.println("SAME INSTRUCTIONS!!");
    }
  }

	/*Read a single Instruction from allRaw array*/
	void XBEE::readInstruct()
	{
    const int MAX_BYTES_PER = 5;
    while (INSTRUCT_BYTE::START_INSTRUCT != static_cast<INSTRUCT_BYTE>(allRawPrevious[rawReadIndex]))
    {
      Serial.println("Im removing garbage");
      rawReadIndex ++;
    }
    for (int i = 0; i <= MAX_BYTES_PER+1; i++)        //Read all the inputs (until stop BYTE is read)
   	{
      rawReadIndex++;
			singleRead[i] = allRawPrevious[rawReadIndex];             //and fill up the temporary array
      Serial.print("Argument # "); Serial.print(i);
      Serial.print(", Raw reading: "); Serial.println(singleRead[i], HEX); 
      if(INSTRUCT_BYTE::END_SINGLE_INSTRUCT == static_cast<INSTRUCT_BYTE>(singleRead[i])) //If Stop BYTE
      {
        break;
  		}
      else if (MAX_BYTES_PER <= i)
      {
        Serial1.println("ERROR-001: Stop BYTE Not Detected");
        while(1){}
      }
   	}                             
	}


  /*Interprets a single raw reading instruction, fills relevant arrays 
   * with the index being the number of instruction */
  void XBEE::interpretInstruct()
  {
    action[instructNum] = singleRead[0]; //add the action to instruction set
    //Serial.print("Instruction Number: "); Serial.println(instructNum);
    //Serial.print("Action: "); Serial.println(action[instructNum] , HEX);
    switch (static_cast<INSTRUCT_BYTE>(action[instructNum]))      //switch between the different types of moves
    {
      case INSTRUCT_BYTE::ACTION_LEFT: //Turn Left
        angle[instructNum] = singleRead[1]; //add the relative turning angle to instruction set
        if (singleRead[2] != 0xF0)          //If the stop BYTE isnt next, something went wrong
        {
          Serial1.println("ERROR-002: Stop BYTE Not Detected as expected"); 
          Serial1.println(singleRead[2], HEX);//print error message
          while(1){}
        }
        break;
      case INSTRUCT_BYTE::ACTION_RIGHT : //Turn Right
        angle[instructNum] = singleRead[1]; //add the turning angle to instruction set
        if (singleRead[2] != 0xF0)          //If the stop BYTE isnt next, something went wrong     
        {
          Serial1.println("ERROR-002: Stop BYTE Not Detected as expected"); //print error message
          Serial1.println(singleRead[2], HEX);
          while(1){}
        }
        break;            
      case INSTRUCT_BYTE::ACTION_FORWARD : //Go Forward
        distance[instructNum] = singleRead[1]; //Add the distance of move to instruction set
        speedy[instructNum] = singleRead[2];   //add the speed of move to instruction set 
        //If the stop BYTE isnt next, something went wrong//if (singleRead[3] != 0xF0)
        if (INSTRUCT_BYTE::END_SINGLE_INSTRUCT != static_cast<INSTRUCT_BYTE>(singleRead[3]))   
        {
          Serial1.println("ERROR-002: Stop BYTE Not Detected as expected"); //print error message
          Serial1.println(singleRead[3], HEX);
          while(1) { }
        }
        break;           
      default: //If the action type is not recognized
        Serial1.println("ERROR-003: Move-type not not recognized"); //print error message
        while(1){}
        break;  
    }
    for (int i = 0; i < 5; i++) //Reset the singleRead array with zeros
    {
      singleRead[i] = 0;
    }
  }

  /* Function that prints full instruction set */
  void XBEE::printInstructSet(int serialPort)
  {
    if (1 == serialPort)
    {
      Serial1.println("Printing all Instructions");
      for (int i = 1; i <= instructTotal; i++) //For each instruction
      {
        Serial1.print("Instruction: "); Serial1.println(i);
        switch (static_cast<INSTRUCT_BYTE>(action[i]))      //switch between the different types of moves
        {
          case INSTRUCT_BYTE::ACTION_LEFT : //Turn Left
            Serial1.println("  Move Type: Left Turn");
            Serial1.print("    Angle: "); Serial1.print(angle[i]); Serial1.println (" degrees");
            break;
          case INSTRUCT_BYTE::ACTION_RIGHT : //Turn Right
            Serial1.println("  Move Type: Right Turn");
            Serial1.print("    Angle: "); Serial1.print(angle[i]); Serial1.println (" degrees");
            break;
          case INSTRUCT_BYTE::ACTION_FORWARD : //Forwarmd
            Serial1.println("  Move Type: Forward");
            Serial1.print("    Distance: "); Serial1.println(distance[i]);
            Serial1.print("    Speed: "); Serial1.println(speedy[i]);
            break;
          default :
            Serial1.print("ERROR-004: Move-type: \""); Serial1.print(action[i], HEX); 
            Serial1.println("\" not recognized");
            while(1){}
        }
      }
    }
    else if (0 == serialPort)
    {
      Serial.println("Printing all Instructions");
      for (int i = 1; i <= instructTotal; i++) //For each instruction
      {
        Serial.print("Instruction: "); Serial.println(i);
        switch (static_cast<INSTRUCT_BYTE>(action[i]))      //switch between the different types of moves
        {
          case INSTRUCT_BYTE::ACTION_LEFT : //Turn Left
            Serial.println("  Move Type: Left Turn");
            Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
            break;
          case INSTRUCT_BYTE::ACTION_RIGHT : //Turn Right
            Serial.println("  Move Type: Right Turn");
            Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
            break;
          case INSTRUCT_BYTE::ACTION_FORWARD : //Forwarmd
            Serial.println("  Move Type: Forward");
            Serial.print("    Distance: "); Serial.println(distance[i]);
            Serial.print("    Speed: "); Serial.println(speedy[i]);
            break;
          default :
            Serial.print("ERROR-004: Move-type: \""); Serial.print(action[i], HEX); 
            Serial.println("\" not recognized");
            while(1){}
        }
      }
    }
  }

  /*Main loop reads xbee data, interpretes it as instucionts and prints them on motior*/
  bool XBEE::getInstructions()
  {
    rawReadIndex = 0;
    readAllRaw();
    
    if (sameInstructFlag)
    {
      return false;
    }
    while (instructNum <= instructTotal && !sameInstructFlag)
    {
      initInstruction();
//      Serial.print("Instruction: "); Serial.print(instructNum); 
//      Serial.print(" Out of: "); Serial.println(instructTotal);
      readInstruct(); //reads a single instruction set from the XBEE
      if (singleRead[0] != 0)       // If an instruction was actually read
      {
        interpretInstruct();   //Function call that interprets the latest instruction and fills global arrays             
        instructNum ++;       //Increment the instruction counter
      }
    }
    printInstructSet(0);   //Prints the entire instruction set
    instructNum = 1;      //reset the instruction counter
    return true;
  }
  
}//NAMESPACE ASAR
