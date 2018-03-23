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
			int action[20] = {0x00};
			int distance[20] ={0x00};
			int angle[20] = {0x00};
			int speedy[20] = {0x00};
      int readFlag = 0; //0 is not read 1 is read

			/*reads xbee data, interpretes it as instucionts and prints them on motior*/
			void getInstructions();




		private:
			int instructTotal = 0;					//total instructions
			int instructNum = 1;            //couner for instruction number initialized to one
			int rawReadIndex = 0;
			uint8_t allRaw[1024] = {0};
			uint8_t singleRead[5] = {0};           //temporary hold place from direct reading of xbee
			void readAllRaw();
			void readInstruct();    //Function that reads xbee and updates insruction variables
			void interpretInstruct(); //Interprets a single instruction and fills global instructions
			void printInstructSet();   //prints all of the instructions
	};
}
#endif
