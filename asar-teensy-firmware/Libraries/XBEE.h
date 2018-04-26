/* XBEE.h
 *  Author: Aaron Mallabar
 *  Date:   March 6,2018
 *  Description: Header file that wraps us the serial commands to read info from the XBEE
 *				and interprets the information into executable directions
 *  
 */

#ifndef XBEE_H
#define XBEE_H

namespace ASAR
{
	class XBEE
	{
		public:
			XBEE();		//Constructor (Should probably take in a baud rate)
			~XBEE();	//Desturctor
			/*Set of arrays that include all the instrctions  *
			 *(index of array is instruction number           */
			int action[256] = {0x00};
			int distance[256] ={0x00};
			int angle[256] = {0x00};
			int speedy[256] = {0x00};
      int instructTotal = 0;          //total instructions
      //int readFlag = 0; //0 is not read 1 is read
      void initInstruction();
			/*reads xbee data, interpretes it as instucionts and prints them on motior*/
		  bool getInstructions(); //Returns true if the instruction is new, returns false if the instruction is duplicate
      enum class INSTRUCT_BYTE
      {
        ACTION_LEFT = 0xAA,
        ACTION_RIGHT = 0xBB,
        ACTION_FORWARD = 0xCC,
        ACTION_STAHP = 0x99,
        END_SINGLE_INSTRUCT = 0xF0,
        END_INSTRUCT_SET = 0xFF,
        START_INSTRUCT = 0xFF,
        DONE_EXECUTION = 0x00
      };

		private:
      const int BAUD_RATE = 115200;
			int instructNum = 1;            //couner for instruction number initialized to one
			int rawReadIndex = 0;
      bool sameInstructFlag = false;
      uint8_t allRawPrevious[1024] = {0};
			uint8_t allRaw[1024] = {0};
			uint8_t singleRead[5] = {0};           //temporary hold place from direct reading of xbee
			void readAllRaw();
			void readInstruct();    //Function that reads xbee and updates insruction variables
			void interpretInstruct(); //Interprets a single instruction and fills global instructions
			void printInstructSet(int serialPort);   //prints all of the instructions
    
	};
}
#endif
