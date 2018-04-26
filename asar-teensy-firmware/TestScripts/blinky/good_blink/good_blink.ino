

#include "PITimer.h"

const int LED = 13;
const double sPeriod = 1; 
double Time = 0;
double othertime = 0;
bool Flag = 0;

void callback();


void setup()
{
  Serial.begin(9600);
  Serial.println("Timer Begin");
  //delay(1000);
  pinMode(LED, OUTPUT);
  PITimer1.period(sPeriod);     // initialize timer1
  PITimer1.start(callback);           // attaches callback() as a timer overflow interrupt

}

void loop()
{
  while (Flag)
  {
    Flag = false;
    Serial.print("timerone: "); Serial.println(Time);
    
  }
}

void callback()
{
  digitalWrite(LED, digitalRead(13) ^ 1);
  Time = Time + sPeriod;
  Flag = true;
}
