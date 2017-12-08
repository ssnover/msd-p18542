/*
 * file: wireless-proto.ino
 * author: Shane Snover
 * purpose: A simple sketch that listens for a byte over Serial and turns
 *          on some LEDs.
 */

#include "Arduino.h"

constexpr uint8_t MESSAGE_ACK(0xaa);


void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  DDRB = 0x3F;
}


void loop()
{
  if (Serial.available())
  {
    volatile uint8_t receivedByte = Serial.read();
    Serial.write(MESSAGE_ACK);
    PORTD ^= (1 << 2);
    PORTB = receivedByte & 0x3F;
  }
  
}

