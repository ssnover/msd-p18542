#include "PITimer.h"
#include "Wire.h"

#define XBEE Serial1

const int LED = 13;
bool Flag = false;
const double sPeriod = 1;
void callback();
void readInstruct();
char xbee_input[4] = {0};

void setup()
{
  Serial.begin(9600);
  XBEE.begin(9600);
  pinMode(LED, OUTPUT);
  PITimer1.period(sPeriod);     // initialize timer1
  PITimer1.start(callback);           // attaches callback() as a timer overflow interrupt
}
int counter = 0;
void loop()
{
  while (Flag)
  {
    readInstruct();
    Serial.println(xbee_input);
    counter ++;
    Flag = false;
  }
}

void callback()
{
  digitalWrite(LED, digitalRead(13) ^ 1);
  Flag = true;
}

void readInstruct()
{
  if (XBEE.available() > 0 && XBEE.read() == 'F' && XBEE.read() == 'F')
  {
    for (int i = 0; i < 5; i++)
    {
      xbee_input[i] = XBEE.read();
    }
  }
  else
  {
   xbee_input[0] = ' ';
   xbee_input[1] = ' ';
   xbee_input[2] = ' ';
   xbee_input[3] = ' ';
   xbee_input[4] = ' ';
  }
 
}
  

