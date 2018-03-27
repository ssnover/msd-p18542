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

  /*Read everything in buffer from XBEE, should be entire instruct set*/
  void XBEE::readAllRaw()
  {
    bool done_flag = false; //flag signaling Completely done with instruction set
    bool start_flag = false; //flag signaling that bits are actuallaly part of instructuin
    int index = 0; //index that cycles through xbee buffer
    instructTotal = 0;
    while (!done_flag)
    { 
      if (Serial1.available())
      {
        allRaw[index] = Serial1.read();
        if (index >= 2 && allRaw[index] == 0xFF && allRaw[index - 1] == 0xFF && allRaw[index - 2] == 0xFF)
        {
          done_flag = true;
          for (int i = 0; i <= 2; i++)
          {
            allRaw[index - i] = 0;
          }
         /* for (int i = 0; i <= index; i++)
          {
            Serial.print(i); Serial.print(". "); Serial.println(allRaw[i], HEX);
          }*/
        }
        else if (allRaw[index] == 0xF0 && start_flag)
        {
          instructTotal++; 
          start_flag = false;
        }
        else if (allRaw[index] == 0xFF)
        {
          start_flag = true;
        }
        index++;
      }
    }
  }



	/*Read a single Instruction from allRaw array*/
	void XBEE::readInstruct()
	{
    while (allRaw[rawReadIndex] != 0xFF)
    {
      //Serial.println("Im removing garbage");
      rawReadIndex ++;
    }
    for (int i = 0; i <= 6; i++)        //Read all the inputs (until stop bit is read)
   	{
      rawReadIndex++;
			singleRead[i] = allRaw[rawReadIndex];             //and fill up the temporary array
//      Serial.print("Argument # "); Serial.print(i);
//      Serial.print(", Raw reading: "); Serial.println(singleRead[i], HEX); 
      if(singleRead[i] == 0xF0) //If Stop bit
      {
        break;
  		}
      else if (i >= 5)
      {
        Serial.println("ERROR-001: Stop Bit Not Detected");
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
    switch (action[instructNum])      //switch between the different types of moves
    {
      case 0xAA : //Turn Left
        angle[instructNum] = singleRead[1]; //add the relative turning angle to instruction set
        if (singleRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;
      case 0xBB : //Turn Right
        angle[instructNum] = singleRead[1]; //add the turning angle to instruction set
        if (singleRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong     
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;            
      case 0xCC : //Go Forward
        distance[instructNum] = singleRead[1]; //Add the distance of move to instruction set
        speedy[instructNum] = singleRead[2];   //add the speed of move to instruction set
        if (singleRead[3] != 0xF0)             //If the stop bit isnt next, something went wrong
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;           
      default: //If the action type is not recognized
        Serial.println("ERROR-003: Move-type not not recognized"); //print error message
        break;  
    }
    for (int i = 0; i < 5; i++) //Reset the singleRead array with zeros
    {
      singleRead[i] = 0;
    }
  }

  /* Function that prints full instruction set */
  void XBEE::printInstructSet()
  {
    Serial.println("Printing all Instructions");
    for (int i = 1; i <= instructTotal; i++) //For each instruction
    {
      Serial.print("Instruction: "); Serial.println(i);
      switch (action[i])      //switch between the different types of moves
      {
        case 0xAA : //Turn Left
          Serial.println("  Move Type: Left Turn");
          Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
          break;
        case 0xBB : //Turn Right
          Serial.println("  Move Type: Right Turn");
          Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
          break;
        case 0xCC : //Forwarmd
          Serial.println("  Move Type: Forward");
          Serial.print("    Distance: "); Serial.println(distance[i]);
          Serial.print("    Speed: "); Serial.println(speedy[i]);
          break;
        default :
          Serial.print("ERROR-003: Move-type: \""); Serial.print(action[i], HEX); 
          Serial.println("\" not recognized");
      }
    }
  }

  /*Main loop reads xbee data, interpretes it as instucionts and prints them on motior*/
  void XBEE::getInstructions()
  {
    rawReadIndex = 0;
    Serial.println("getting all instructions");
    readAllRaw();
    while (instructNum <= instructTotal)
    {
      //Serial.print("Instruction: "); Serial.print(instructNum); 
      //Serial.print(" Out of: "); Serial.println(instructTotal);
      readInstruct();         //reads a single instruction set from the XBEE
      if (singleRead[0] != 0)       // If an instruction was actually read
      {
        interpretInstruct();   //Function call that interprets the latest instruction and fills global arrays             
        instructNum ++;       //Increment the instruction counter
      }
    }
    printInstructSet();   //Prints the entire instruction set
    instructNum = 1;      //reset the instruction counter
  }
  
}//NAMESPACE ASAR
