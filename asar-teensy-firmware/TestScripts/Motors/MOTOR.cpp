/* Motor.cpp
 *  Author: Aaron Mallabar
 *  Date:   January 22,2018
 *  Description: Low Level Motor Control
 *  
 */
 

//Teensy Pinout
//RightA is forward
//LeftB is forward

#include "Arduino.h"
#include "MOTOR.h"


namespace ASAR
{
MOTOR::MOTOR()
{
	pinMode(this->enablepin_right, OUTPUT);
	pinMode(this->enablepin_left, OUTPUT);
	pinMode(this->PWM_LeftA, OUTPUT);
	pinMode(this->PWM_LeftB, OUTPUT);
	pinMode(this->PWM_RightA, OUTPUT);
	pinMode(this->PWM_RightB, OUTPUT);
	
}

MOTOR::~MOTOR()
{
	//Empty Destructor
}




void MOTOR::Forward(const int Speed)
{
	auto PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
 
	analogWrite(this->PWM_RightA, PWMval);
	analogWrite(this->PWM_RightB, 0);
	analogWrite(this->PWM_LeftA, 0);
	analogWrite(this->PWM_LeftB, PWMval);

    
}

  
void MOTOR::Backwards(const int Speed)
{
	auto PWMval = Speed * 50; //Convert Speed Setting to PWM Val

	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, 0);
	analogWrite(this->PWM_RightB, PWMval);
	analogWrite(this->PWM_LeftA,  PWMval);
	analogWrite(this->PWM_LeftB, 0);
    
}
  
void MOTOR::RightTurn(const int Speed)
{
	auto PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, PWMval);
	analogWrite(this->PWM_RightB,0);
	analogWrite(this->PWM_LeftA, PWMval);
	analogWrite(this->PWM_LeftB, 0);
    
}

void MOTOR::LeftTurn(const int Speed)
{
	auto PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, 0);
	analogWrite(this->PWM_RightB,PWMval);
	analogWrite(this->PWM_LeftA, 0);
	analogWrite(this->PWM_LeftB, PWMval);
    
}

void MOTOR::Stop()
{
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, 0);
	analogWrite(this->PWM_RightB, 0);
	analogWrite(this->PWM_LeftA, 0);
	analogWrite(this->PWM_LeftB, 0);
    
}
} // namespace ASAR



