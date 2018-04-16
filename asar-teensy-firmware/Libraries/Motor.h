/*
 * file: Motor.h
 * purpose: Low-Level Control of Motors
 */
 
 #ifndef MOTOR_H
 #define MOTOR_H

#include "Encoder.h"
 
 namespace ASAR
 {
	 class MOTOR
	 {
		 public: 
		
			MOTOR();
			~MOTOR();
			void Forward(const int Speed);
			void Backwards(const int Speed);
			void RightTurn(const int Speed);
			void LeftTurn(const int Speed);
      int errorAdjust();
			void Stop();
      double getPosition();
      double getAngle();
      void initEncoder();
      
    
    
    void ReadCounts(); //Hand describes left hand side 'l' or right hand side 'r'
		
      		
			
		 
		 private:
		 
			const int enablepin_right = 8; 
			const int enablepin_left =  7;
			const int PWM_LeftB = 3;
			const int PWM_RightB = 4;
			const int PWM_RightA = 5; 
			const int PWM_LeftA = 6;
			const int encoderA1 = 16;  //1 = Left
			const int encoderA2 = 15;	 //2 = Right
			const int encoderB1 = 17;
			const int encoderB2 = 14;

           /*These things should be private later*/
      double LeftCounts = 0;
      double RightCounts = 0;
      double Lrevs = 0;
      double Rrevs = 0;

		 
	 }; //MOTOR_H
 }
 #endif
		 
