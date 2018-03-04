#include "PITimer.h"
#include "Wire.h"

#define XBEE Serial1

const int LED = 13;         //Debug LED
bool Flag = false;          //Flag to start loop
const double sPeriod = .1;  //Period at which loop runs
void callback();            //Interrupt function starting the loop
void readInstruct();        //Function that reads xbee and updates insruction variables

void setup()
{
  Serial.begin(9600);       //Initialize Serial Monitor w/ baud rate
  XBEE.begin(9600);         //Initialize Xbee, with baud rate
  pinMode(LED, OUTPUT);     //Initialize LED as output
  PITimer1.period(sPeriod); // initialize timer1
  PITimer1.start(callback); // attaches callback() as a timer overflow interrupt
}

/*Main loop reads xbee and updates instructions to robot calling the readInstruct function*/
void loop()
{
  while (Flag)              //Run the loop only when flag (from callback) is raised
  {
    readInstruct();         //read the instructions from xbee
    Flag = false;           //lower the flag so loop doesnt run again until time
  }
}

/*callback function is interrupt function that tells the loop when it is time to run. *
* It gets called every sPeriod Seconds                                                */
void callback()                                     
{
  digitalWrite(LED, digitalRead(13) ^ 1); //toggle LED
  Flag = true;                            //Raise Flag
}


/*Read Instruction from xbee*/
void readInstruct()
{
  int reading[5] = {0};               //temporary hold place from direct reading of xbee
  if (XBEE.available())               //Only if there is something from xbee to read
  {
    if (XBEE.read() == 0xFF)           //Start reading, if the start bit is read
    {
      for (int i=0; i <= 3; i++)          //Read the next four inputs
      {
        reading[i] = XBEE.read();             //and fill up the temportaryarray
      }                                   //end of instruction
      switch (reading[0])
      {
        case 0xAA :
          Serial.print("Turn Left for");
          break;
        case 0xBB :
          Serial.print("Turn Right for");
          break;            
        case 0xCC :
          Serial.println("March at");
          break;          
        case 0x00 :
          Serial.println("Stop!!");
          break;    
        default: 
          Serial.println("Error, Something with wrong with the communication!");
          break;      
      }                                  
    }                                
  }
}
  

