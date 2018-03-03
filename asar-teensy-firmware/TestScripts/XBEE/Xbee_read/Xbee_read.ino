#include "Wire.h"

#define XBEE Serial1

const int ledpin = 13;
char xbee_input;



void setup()
{
  Serial.begin(9600);
  XBEE.begin(9600);
  pinMode(ledpin, OUTPUT);
}

void loop()
{
  digitalWrite(ledpin, HIGH);
  if(XBEE.available() > 0)
  {
  	xbee_input = XBEE.read();
  	Serial.print(xbee_input);
  }
}

