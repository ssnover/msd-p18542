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
  digitalWrite(ledpin, LOW);
  XBEE.print("a");
  Serial.println("Writing..");
  delay(500);
  digitalWrite(ledpin, HIGH);
  delay(500);
}

