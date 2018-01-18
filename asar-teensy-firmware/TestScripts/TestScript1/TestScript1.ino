/* TestScript1.ino
 *
 *  Author: Aaron Mallabar
 *  Date:   January 18,2017
 *  Description: Start Testing some of the capabilities of our MSD prototype Robot PCB.
 *  1. Starting with a blink LED
 *  2. Motor Movement
 *  
 */
 
const int led = 13;
const int delaytime = 100;

const int enablepin_right = 8;
const int enablepin_left =  7;
const int PWM_LeftB = 3;
const int PWM_RightB = 4;
const int PWM_RightA = 5; 
const int PWM_LeftA = 6;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(enablepin_right, OUTPUT);
  pinMode(enablepin_left, OUTPUT);
  pinMode(PWM_LeftA, OUTPUT);
  pinMode(PWM_LeftB, OUTPUT);
  pinMode(PWM_RightA, OUTPUT);
  pinMode(PWM_RightB, OUTPUT);

}

void loop()
{
  BlinkLED();
  Forward(5000, 255);
}

void BlinkLED()
{

  digitalWrite(led, HIGH);
  delay(delaytime);
  digitalWrite(led, LOW);
  delay(delaytime);
}

void Forward(const int Time, const int Speed)
{
  digitalWrite(enablepin_right, HIGH);
  digitalWrite(enablepin_left, HIGH);
  
  digitalWrite(PWM_RightA, HIGH);
  digitalWrite(PWM_RightB, LOW);

  digitalWrite(PWM_LeftA, LOW);
  digitalWrite(PWM_LeftB, HIGH);
  
  delay(Time);

  digitalWrite(PWM_RightA, LOW);
  digitalWrite(PWM_RightB, LOW);

  digitalWrite(PWM_LeftA, LOW);
  digitalWrite(PWM_LeftB, LOW);
  
  
}

