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
namespace
{
	const int COUNTS_PER_REV = 48*34; //48 Counts per motor rev * N=34 Gear output
	const int WHEEL_RADIUS = 45; //mm
  const int ROBOT_RADIUS = 85; //mm 
  Encoder LeftEncoder(16, 17);
  Encoder RightEncoder(15, 14);
}
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
	int PWMval = Speed; //Convert Speed Setting to PWM Val
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
 
	analogWrite(this->PWM_RightA, PWMval);
	analogWrite(this->PWM_RightB, 0);
	analogWrite(this->PWM_LeftA, 0);
	analogWrite(this->PWM_LeftB, PWMval);

    
}

  
void MOTOR::Backwards(const int Speed)
{
	int PWMval = Speed; //Convert Speed Setting to PWM Val

	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, 0);
	analogWrite(this->PWM_RightB, PWMval);
	analogWrite(this->PWM_LeftA,  PWMval);
	analogWrite(this->PWM_LeftB, 0);
    
}
  
void MOTOR::RightTurn(const int Speed)
{
	int PWMval = Speed; //Convert Speed Setting to PWM Val
	digitalWrite(this->enablepin_right, HIGH);
	digitalWrite(this->enablepin_left, HIGH);
  
	analogWrite(this->PWM_RightA, PWMval);
	analogWrite(this->PWM_RightB,0);
	analogWrite(this->PWM_LeftA, PWMval);
	analogWrite(this->PWM_LeftB, 0);
    
}

void MOTOR::LeftTurn(const int Speed)
{
	int PWMval = Speed; //Convert Speed Setting to PWM Val
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

void MOTOR::ReadCounts()
{

	LeftCounts = -LeftEncoder.read();
	RightCounts = RightEncoder.read();

}

double MOTOR::getPosition()
{
	ReadCounts();
	Lrevs = LeftCounts / COUNTS_PER_REV;
  Rrevs = RightCounts / COUNTS_PER_REV;
  double pos = 0;
  double revs = (Lrevs + Rrevs) / 2;
  pos =  revs * 2* PI * WHEEL_RADIUS; //mm
  return pos;

}

double MOTOR::getAngle()
{
  ReadCounts();
  Lrevs = LeftCounts / COUNTS_PER_REV;
  Rrevs = RightCounts / COUNTS_PER_REV; 
  double angle = 0;
  angle = ((Lrevs+Rrevs)/2)*(WHEEL_RADIUS/ROBOT_RADIUS)*360;
  return angle;
  
}

void MOTOR::initEncoder()
{
  LeftEncoder.write(0);
  RightEncoder.write(0);
}

} // namespace ASAR



