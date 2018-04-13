#include "Wire.h"

//const auto XBEE = Serial1.

const int ledpin = 13;
char* xbee_input = "Hello";



void setup()
{
  Serial.begin(9600);
  //XBEE.begin(9600);
  pinMode(ledpin, OUTPUT);
}

void loop()
{
  digitalWrite(ledpin, LOW);
  //XBEE.print(xbee_input);
  Serial.print("Writing: "); Serial.println(xbee_input);
  delay(1000);
  digitalWrite(ledpin, HIGH);
  delay(1000);

}

