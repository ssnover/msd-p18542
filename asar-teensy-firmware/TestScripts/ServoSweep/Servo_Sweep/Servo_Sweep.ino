

#include <Servo.h>
#include "PITimer.h"

const int LED = 13;
const int servoPin = 9;
const double sPeriod = .01;
double Time = 0;
bool Flag = 0;

Servo myServo;

void callback();
void ServoSweep();


void setup()
{
  Serial.begin(9600);
  Serial.println("Timer Begin");
  pinMode(LED, OUTPUT);
  myServo.attach(servoPin);
  PITimer1.period(sPeriod);     // initialize timer1
  PITimer1.start(callback);           // attaches callback() as a timer overflow interrupt

}

void loop()
{
  while (Flag)
  {
    Flag = false;
    ServoSweep();
  }
}

void callback()
{
    if (!Flag)
    {
      Serial.println("Error: Didn't Get to Bottom of Loop");
    }
  digitalWrite(LED, !digitalRead(LED));
  Flag = true;
}

void ServoSweep()
{
  int pos = 0;
  for (pos = 0; pos <= 180; pos += 1)  // goes from 0 degrees to 180 degrees
                                        // in steps of 1 degree
  {
    myServo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myServo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  
}


