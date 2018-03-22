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
		Serial1.begin(9600);      	//Initialize Xbee, with baud rate
	}

	XBEE::~XBEE()
	{
		//empty destructor
	}

  /*Read everything in buffer from XBEE, should be entire instruct set*/
  void XBEE::readAllRaw()
  {
    bool done_flag = false;
    int index = 0;
    while (!done_flag)
    { 
      if (Serial1.available())
      {
        allRaw[index] = Serial1.read();
       // Serial.print("Reading: "); Serial.println(allRaw[index], HEX);
        if (index >= 2 && allRaw[index] == 0xFF && allRaw[index - 1] == 0xFF && allRaw[index - 2] == 0xFF)
        {
          done_flag = true;
          instructTotal = index;
        }
        index++;
      }
    }
  }



	/*Read a single Instruction from allRaw array*/
	void XBEE::readInstruct()
	{
    Serial.println("Reading First Instruct");
	  if (allRaw[byteCounter] == 0xFF)               //Only if something was actually ready by the xbee
	  {
	    byteCounter++;
	    for (int i = 0; i <= 6; i++)        //Read all the inputs (until stop bit is read)
	   	{
				singleRead[i] = allRaw[byteCounter];             //and fill up the temporary array
        byteCounter++;
	      Serial.print("Argument # "); Serial.print(i);
	      Serial.print(", Raw reading: "); Serial.println(singleRead[i], HEX); 
	      if(singleRead[i] == 0xF0)
	      {
          break;
	  		}
	      else if (i >= 5)
	      {
	        Serial.println("ERROR-001: Stop Bit Not Detected");
	      }
	   	}
  	}                                  
	}


  /*Interprets a single raw reading instruction, fills relevant arrays 
   * with the index being the number of instruction */
  void XBEE::interpretInstruct()
  {
    Serial.println("Interpretting the Instruction");
    action[instructNum] = singleRead[0]; //add the action to instruction set
    Serial.print("Instruction Number: "); Serial.println(instructNum);
    Serial.print("Action: "); Serial.println(action[instructNum] , HEX);
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
    for (int i = 1; i <= instructNum; i++) //For each instruction
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
          Serial.println("ERROR-003: Move-type not not recognized");
      }
    }
  }

  /*Main loop reads xbee data, interpretes it as instucionts and prints them on motior*/
  void XBEE::getInstructions()
  {
    Serial.println("Reading all insturctions");
    readAllRaw();
    readInstruct();         //reads a single instruction set from the XBEE
    if (singleRead[1] != 0)       // If an instruction was actually read
    {
      interpretInstruct();   //Function call that interprets the latest instruction and fills global arrays      
      if (instructNum >= instructTotal) //If last instuction was read and intepretted
      {
        printInstructSet();   //Prints the entire instruction set
        instructNum = 1;      //reset the instruction counter
      }
      else                    //Otherwise (not the last instruction)
      {
        instructNum ++;       //Increment the instruction counter
      }
    }
  }

}
