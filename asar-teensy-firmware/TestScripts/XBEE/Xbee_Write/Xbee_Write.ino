#include <SoftwareSerial.h>

SoftwareSerial XBee(2, 3); // RX, TX

void SendInstruct(int Action, int distance, int spd);
void Forward();
void Turn();

void setup()
{
  // Set up both ports at 9600 baud. This value is most important
  // for the XBee. Make sure the baud rate matches the config
  // setting of your XBee.
  XBee.begin(115200);
  Serial.begin(115200);
  delay(100);
  Serial.println("Sending...");
  Forward();
  //Turn();
}

void SendInstruct(int Action, int distance, int spd)
{
  XBee.write(255); 
  switch (Action)
  {
    case 1:
      XBee.write(204);
      XBee.write(distance);
      XBee.write(spd);
      break;
    case 2:
      XBee.write(170);
      break;
    default:
      XBee.write("OOPS"); 
  }
   XBee.write(240); 
   XBee.write(255); 
   XBee.write(255); 
   XBee.write(255); 
  
}

void Forward()
{
  Serial.println("Here");
  XBee.write(255);//Start
  XBee.write(204);//Forward //204:Forward  //170: 
  XBee.write(100);//100 cm
  XBee.write(200); //100 spd
  XBee.write(240);//done instruct
  XBee.write(255);XBee.write(255);XBee.write(255);
}

void Turn()
{
  XBee.write(255);//Start
  XBee.write(170);
  XBee.write(180);
  XBee.write(240);//done instruct
  XBee.write(255);XBee.write(255);XBee.write(255);
}

void loop()
{
//  if (Serial.available())
//  { // If data comes in from serial monitor, send it out to XBee
//    XBee.write(255);
//  }
  if (XBee.available())
  { // If data comes in from XBee, send it out to serial monitor
    Serial.write(XBee.read());
  }
}
