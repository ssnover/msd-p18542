/*
 * file: Motor.h
 * purpose: Low-Level Control of Motors
 */
 
 #ifndef MOTOR_H
 #define MOTOR_H
 
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
			void Stop();
			
			
		 
		 private:
		 
			const int enablepin_right = 8; 
			const int enablepin_left =  7;
			const int PWM_LeftB = 3;
			const int PWM_RightB = 4;
			const int PWM_RightA = 5; 
			const int PWM_LeftA = 6;
		 
	 };
 }
 #endif
		 