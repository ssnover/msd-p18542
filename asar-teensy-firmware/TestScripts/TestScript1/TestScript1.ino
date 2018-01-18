/* TestScript1.ino
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

const int EncoderB1 = 17;
const int EncoderA1 = 16;
const int EncoderA2 = 15;
const int EncoderB2 = 14;


void setup()
{
  pinMode(led, OUTPUT);
  pinMode(enablepin_right, OUTPUT);
  pinMode(enablepin_left, OUTPUT);
  pinMode(PWM_LeftA, OUTPUT);
  pinMode(PWM_LeftB, OUTPUT);
  pinMode(PWM_RightA, OUTPUT);
  pinMode(PWM_RightB, OUTPUT);
  pinMode(EncoderA1, INPUT);
  pinMode(EncoderA2, INPUT);
  pinMode(EncoderB1, INPUT);
  pinMode(EncoderB2, INPUT);
  Serial.begin(9600);

}

void loop()
{
  //BlinkLED();
  //Forward(5000, 100);
  readEncoders();
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
  
  analogWrite(PWM_RightA, Speed);
  analogWrite(PWM_RightB, 0);
  analogWrite(PWM_LeftA, 0);
  analogWrite(PWM_LeftB, Speed);
  
  delay(Time);

  analogWrite(PWM_RightA, 0);
  analogWrite(PWM_RightB, 0);
  analogWrite(PWM_LeftA, 0);
  analogWrite(PWM_LeftB, 0);
  
  
}

void readEncoders()
{
  const int speedWrite = 255;
  int a1Val = 0;
  int a2Val = 0;
  int b1Val = 0;
  int b2Val = 0;
  
  digitalWrite(enablepin_right, HIGH);
  digitalWrite(enablepin_left, HIGH);
  
  analogWrite(PWM_RightA, speedWrite);
  analogWrite(PWM_RightB, 0);
  analogWrite(PWM_LeftA, 0);
  analogWrite(PWM_LeftB, speedWrite);

  a1Val = analogRead(EncoderA1);
  a2Val = analogRead(EncoderA2);
  b1Val = analogRead(EncoderB1);
  b2Val = analogRead(EncoderB2);

  Serial.print("A1: "); Serial.println(a1Val); 
  Serial.print("A2: "); Serial.println(a2Val);
  Serial.print("B1: "); Serial.println(b1Val);  
  Serial.print("B2: "); Serial.println(b2Val); 

  delay(500);

  

  

  

}

