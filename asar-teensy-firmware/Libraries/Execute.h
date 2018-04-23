/*
 * ExecuteInstructs.H
 * Author: Aaron Mallabar
 * Date: March 20, 2018
 * Description: This Script takes in a set of instructions from the xbee.
 *              And executes the instructions using the the encoder. 
 *              
 *          
 */
 
 #ifndef EXECUTE_H
 #define EXECUTE_H

#include "Arduino.h"
#include "Motor.h"
#include "XBEE.h"

 
 namespace ASAR
 {
	 class EXECUTE
	 {
		 public: 
		
			EXECUTE();
			~EXECUTE();
			void execute();

		 private:

		 	const int LED = 13;
		 	bool instructDone = true;
		 	bool printedReady = false;
		 	bool readyForNew = true;
		 	int CurrentInstruct = 1;
			double displacement = 0;
			double angle = 0;
      const double angleError = 0;
      const double displacementError = 0;
			const int TURN_SPEED = 220;
      const int INSTRUCTION_2_INSTRUCTION_DELAY = 250; //milliseconds

			void executeSetup();		 
			void executeCurrentInstruct();
			void printStatus(int serialPort);

      XBEE myXBEE;
      MOTOR myMOTOR;



		 
	 }; //EXECUTE_H
 }
 #endif
		 
