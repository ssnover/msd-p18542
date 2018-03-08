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
		Serial1.begin(115200);      	//Initialize Xbee, with baud rate
	}

	XBEE::~XBEE()
	{
		//empty destructor
	}

	/*Read a single Instruction from xbee*/
	void XBEE::readRawInstruct()
	{
	  if (Serial1.available() && Serial1.read() == 0xFF)               //Only if there is something from xbee to read
	  {
	    for (int i = 0; i <= 5; i++)        //Read all the inputs (until stop bit is read)
	   	{
				rawRead[i] = Serial1.read();             //and fill up the temporary array
	      	//Serial.print("Argument # "); Serial.print(i);
	      	//Serial.print(", Raw reading: "); Serial.println(rawRead[i], HEX); 
	      if(rawRead[i] == 0xF0)
	      {
	       	i = 6;
	  		}
	      else if (i >= 4)
	      {
	        Serial.println("ERROR-001: Stop Bit Not Detected");
	      }
	   	}
  	}                                   
	}


  /*Interprets a single raw reading instruction, fills relevant arrays 
   * with the index being the number of instruction */
  void XBEE::Interpret_instruct()
  {
    action[instructNum] = rawRead[0]; //add the action to instruction set
    switch (action[instructNum])      //switch between the different types of moves
    {
      case 0xAA : //Turn Left
        angle[instructNum] = rawRead[1]; //add the relative turning angle to instruction set
        if (rawRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;
      case 0xBB : //Turn Right
        angle[instructNum] = rawRead[1]; //add the turning angle to instruction set
        if (rawRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong     
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;            
      case 0xCC : //Go Forward
        distance[instructNum] = rawRead[1]; //Add the distance of move to instruction set
        speedy[instructNum] = rawRead[2];   //add the speed of move to instruction set
        if (rawRead[3] != 0xF0)             //If the stop bit isnt next, something went wrong
        {
          Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
        }
        break;           
      default: //If the action type is not recognized
        Serial.println("ERROR-003: Move-type not not recognized"); //print error message
        break;  
    }
    for (int i = 0; i < 5; i++) //Reset the rawread array with zeros
    {
      rawRead[i] = 0;
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
  void XBEE::GetInstructions(int expectedNumInstructions)
  {
    readRawInstruct();         //reads a single instruction set from the XBEE
    if (rawRead[0] != 0)       // If an instruction was actually read
    {
      Interpret_instruct();   //Function call that interprets the latest instruction and fills global arrays      
      if (instructNum >= expectedNumInstructions) //If last instuction was read and intepretted
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
