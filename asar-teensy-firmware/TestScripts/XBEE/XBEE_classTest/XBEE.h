/* XBEE.h
 *  Author: Aaron Mallabar
 *  Date:   March 6,2018
 *  Description: Header file that wraps us the serial commands to read info from the XBEE
 *				and interprets the information into executable directions
 *  
 */

#ifdef XBEE_H
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

			/*reads xbee data, interpretes it as instucionts and prints them on motior*/
			void GetInstructions(int expectedNumInstructions);




		private:

			int instructNum = 1;            //couner for instruction number initialized to one
			int rawRead[5] = {0};           //temporary hold place from direct reading of xbee

			void readRawInstruct();    //Function that reads xbee and updates insruction variables
			void Interpret_instruct(); //Interprets a single instruction and fills global instructions
			void printInstructSet();   //prints all of the instructions
	};
}
#endif