

#include "PITimer.h"

const int LEDpin = 13;
const int trigPin = 21;
const int echoPin = 20;
const double sPeriod = .1; 
double Time = 0;
bool Flag = 0;
auto obstacleDist = 0;

void callback();
int CheckPing(); //Returns distance

void setup()
{
  Serial.begin(9600);
  Serial.println("Timer Begin");
  //delay(1000);
  pinMode(LEDpin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  PITimer1.period(sPeriod);     // initialize timer1
  PITimer1.start(callback);           // attaches callback() as a timer overflow interrupt

}

void loop()
{

  while (Flag)
  {
    Flag = false;
    obstacleDist = CheckPing();
    Serial.println(obstacleDist);
    if (obstacleDist <= 10)
    {
      digitalWrite(LEDpin, HIGH);
    }
    else 
    {
      digitalWrite(LEDpin, LOW);
    }
    
  }

}

void callback()
{
  //digitalWrite(LEDpin, digitalRead(13) ^ 1);
  Time = Time + sPeriod;
  Flag = true;
}

int CheckPing()
{
  int duration = 0;
  double distance = 0;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2;
  return distance;
}

