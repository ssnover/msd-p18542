/* MotorClass
 *  Author: Aaron Mallabar
 *  Date:   January 22,2018
 *  Description: Low Level Motor Control
 *  
 */
 

//Teensy Pinout
//RightA is forward
//LeftB is forward

const int enablepin_right = 8; 
const int enablepin_left =  7;
const int PWM_LeftB = 3;
const int PWM_RightB = 4;
const int PWM_RightA = 5; 
const int PWM_LeftA = 6;

void Motor_init()
{
	pinMode(led, OUTPUT);
	pinMode(enablepin_right, OUTPUT);
	pinMode(enablepin_left, OUTPUT);
	pinMode(PWM_LeftA, OUTPUT);
	pinMode(PWM_LeftB, OUTPUT);
	pinMode(PWM_RightA, OUTPUT);
	pinMode(PWM_RightB, OUTPUT);
}


void Forward(const int Speed)
{
	PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	
	digitalWrite(enablepin_right, HIGH);
	digitalWrite(enablepin_left, HIGH);
 
	analogWrite(PWM_RightA, PWMval);
	analogWrite(PWM_RightB, 0);
	analogWrite(PWM_LeftA, 0);
	analogWrite(PWM_LeftB, PWMval);
    
}

  
void Backwards(const int Speed)
{
	PWMval = Speed * 50; //Convert Speed Setting to PWM Val

	digitalWrite(enablepin_right, HIGH);
	digitalWrite(enablepin_left, HIGH);
  
	analogWrite(PWM_RightA, 0);
	analogWrite(PWM_RightB, PWMval);
	analogWrite(PWM_LeftA,  PWMval);
	analogWrite(PWM_LeftB, 0);
    
}
  
void RightTurn(const int Speed)
{
	PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	digitalWrite(enablepin_right, HIGH);
	digitalWrite(enablepin_left, HIGH);
  
	analogWrite(PWM_RightA, PWMval);
	analogWrite(PWM_RightB,0);
	analogWrite(PWM_LeftA, PWMval);
	analogWrite(PWM_LeftB, 0);
    
}

void LeftTurn(const int Speed)
{
	PWMval = Speed * 50; //Convert Speed Setting to PWM Val
	digitalWrite(enablepin_right, HIGH);
	digitalWrite(enablepin_left, HIGH);
  
	analogWrite(PWM_RightA, 0);
	analogWrite(PWM_RightB,PWMval);
	analogWrite(PWM_LeftA, 0);
	analogWrite(PWM_LeftB, PWMval);
    
}

void Stop()
{
	digitalWrite(enablepin_right, HIGH);
	digitalWrite(enablepin_left, HIGH);
  
	analogWrite(PWM_RightA, 0);
	analogWrite(PWM_RightB, 0);
	analogWrite(PWM_LeftA, 0);
	analogWrite(PWM_LeftB, 0);
    
}



