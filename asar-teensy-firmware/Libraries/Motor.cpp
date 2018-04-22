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
#include "Motor.h"

namespace ASAR
{
  
  namespace
  {
  	const int COUNTS_PER_REV = 48*34; //48 Counts per motor rev * N=34 Gear output
  	const float WHEEL_RADIUS = 4.5 + .75; //cm
    const float ROBOT_RADIUS = 8.5+6.7; //cm
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
    double Adjust = forwardErrorAdjust();
    //double Adjust = 0;
  	double PWMval_left = Speed + Adjust; //Convert Speed Setting to PWM Val
    double PWMval_right = Speed - Adjust;
//    Serial.print("Adjust: "); Serial.print(Adjust);
//    Serial.print("  PWM Left: "); Serial.print(PWMval_left);
//    Serial.print("  PWM Right: "); Serial.println(PWMval_right);
  	digitalWrite(this->enablepin_right, HIGH);
  	digitalWrite(this->enablepin_left, HIGH);
   
  	analogWrite(this->PWM_RightA, PWMval_right);
  	analogWrite(this->PWM_RightB, 0);
  	analogWrite(this->PWM_LeftA, 0);
  	analogWrite(this->PWM_LeftB, PWMval_left);
  }
  
    
  void MOTOR::Backwards(const int Speed)
  {
    int Adjust = forwardErrorAdjust();
    int PWMval_left = Speed - Adjust; //Convert Speed Setting to PWM Val
    int PWMval_right = Speed + Adjust;
//  	Serial1.print("Adjust: "); Serial1.println(Adjust);
//    Serial1.print("PWM Left: "); Serial1.println(PWMval_left);
//    Serial1.print("PWM Right: "); Serial1.println(PWMval_right);
  	digitalWrite(this->enablepin_right, HIGH);
  	digitalWrite(this->enablepin_left, HIGH);
    
  	analogWrite(this->PWM_RightA, 0);
  	analogWrite(this->PWM_RightB, PWMval_right);
  	analogWrite(this->PWM_LeftA,  PWMval_left);
  	analogWrite(this->PWM_LeftB, 0);
      
  }
    
  void MOTOR::RightTurn(const int Speed)
  {
  	int Adjust = rightErrorAdjust();
    //Adjust =0;
    int PWMval_left = Speed + Adjust; //Convert Speed Setting to PWM Val
    int PWMval_right = Speed - Adjust;
//    Serial1.print("Adjust: "); Serial1.println(Adjust);
//    Serial1.print("PWM Left: "); Serial1.println(PWMval_left);
//    Serial1.print("PWM Right: "); Serial1.println(PWMval_right);
  	digitalWrite(this->enablepin_right, HIGH);
  	digitalWrite(this->enablepin_left, HIGH);
    
  	analogWrite(this->PWM_RightA, PWMval_right);
  	analogWrite(this->PWM_RightB,0);
  	analogWrite(this->PWM_LeftA, PWMval_left);
  	analogWrite(this->PWM_LeftB, 0);
      
  }
  
  void MOTOR::LeftTurn(const int Speed)
  {
    int Adjust = leftErrorAdjust();
    int PWMval_left = Speed - Adjust; //Convert Speed Setting to PWM Val
    int PWMval_right = Speed + Adjust;
    if ( PWMval_left >= 255 )
    {
      PWMval_left = 255;
      PWMval_right = PWMval_right + Adjust;
    }
    else if ( PWMval_left <= 0 )
    {
      PWMval_left = 0;
      PWMval_right = PWMval_right + Adjust;
    }
    if ( PWMval_right >= 255 )
    {
      PWMval_right = 255;
      PWMval_left = PWMval_left - Adjust;
    }
    else if ( PWMval_right <= 0 )
    {
      PWMval_right = 0;
      PWMval_left = PWMval_left - Adjust;
    }
//  	Serial.print("Adjust: "); Serial.println(Adjust);
//    Serial.print("PWM Left: "); Serial.println(PWMval_left);
//    Serial.print("PWM Right: "); Serial.println(PWMval_right);
  	digitalWrite(this->enablepin_right, HIGH);
  	digitalWrite(this->enablepin_left, HIGH);
    
  	analogWrite(this->PWM_RightA, 0);
  	analogWrite(this->PWM_RightB,PWMval_right);
  	analogWrite(this->PWM_LeftA, 0);
  	analogWrite(this->PWM_LeftB, PWMval_left);
      
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
//    Serial.print("Left: "); Serial.print(LeftCounts);
//    Serial.print( "Right: "); Serial.println(RightCounts);
  }

  int MOTOR::forwardErrorAdjust()
  {
    double Error = 0;
    ReadCounts();
    Error = ((LeftCounts) - (RightCounts));
//    Serial.print("Left Counts: "); Serial.print(LeftCounts); 
//    Serial.print("  Right Counts: "); Serial.print(RightCounts);
//    Serial.print("  Error: "); Serial.println(Error);
    return Error;
  }

  int MOTOR::leftErrorAdjust()
  {
    double Error = 0;
    ReadCounts();
    Error = ((LeftCounts) + (RightCounts));
//    Serial.print("Left Counts: "); Serial.print(LeftCounts); 
//    Serial.print("  Right Counts: "); Serial.print(RightCounts);
//    Serial.print("  Error: "); Serial.println(Error);
    return Error;
  }

  int MOTOR::rightErrorAdjust()
  {
    double Error = 0;
    ReadCounts();
  //  Error = ((LeftCounts) + (RightCounts));
//    Serial.print("Left Counts: "); Serial.print(LeftCounts); 
//    Serial.print("  Right Counts: "); Serial.print(RightCounts);
//    Serial.print("  Error: "); Serial.println(Error);
    return Error;
  }
  
  double MOTOR::getPosition()
  {
  	ReadCounts();
  	Lrevs = LeftCounts / COUNTS_PER_REV;
    Rrevs = RightCounts / COUNTS_PER_REV;
    double pos = 0;
    double revs = (Lrevs + Rrevs) / 2;
    pos =  revs * 2* PI * WHEEL_RADIUS; //cm
    return pos;
  
  }
  
  double MOTOR::getAngle()
  {
    ReadCounts();
    Lrevs = LeftCounts / COUNTS_PER_REV;
    Rrevs = RightCounts / COUNTS_PER_REV;
    //Serial.print("Rrevs: "); Serial.println(Rrevs); 
    double angle = 0;
    angle = ((Lrevs-Rrevs)/2)*(WHEEL_RADIUS/ROBOT_RADIUS)*360;
    return angle;
    
  }
  
  void MOTOR::initEncoder()
  {
    LeftEncoder.write(0);
    RightEncoder.write(0);
  }

} // namespace ASAR



