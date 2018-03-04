#include "PITimer.h"
#include "Wire.h"

#define XBEE Serial1

const int LED = 13;         //Debug LED
bool Flag = false;          //Flag to start loop
const double sPeriod = .1;  //Period at which loop runs
void callback();            //Interrupt function starting the loop
void readInstruct();        //Function that reads xbee and updates insruction variables
void printInstructSet();    //Prints all available instructions

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
  int instructCounter = 0;
  int action[20] = {0x00};
  int distance[20] ={0x00};
  int angle[20] = {0x00};
  int speedy[20] = {0x00};
  if (XBEE.available())               //Only if there is something from xbee to read
  {
    if (XBEE.read() == 0xFF)           //Start reading, if the start bit is read
    {
      instructCounter ++; 
      for (int i=0; i <= 0xFF; i++)          //Read all the inputs (until stop bit is read)
      {
        reading[i] = XBEE.read();             //and fill up the temportaryarray
        if (reading[i] == 0xF0)               //If read stop byte
        {
          break;                                  //Break FOR loop (stop reading)
        }
        else if(i > 5)                        //If Stop bit not read by expected time
        {
          Serial.println("Error");               //Send Error Message   
        }
      }                                   //end of instruction
      action[instructCounter] = reading[0]; //add the action to instruction set
      switch (action[instructCounter])      //switch between the different types of moves
      {
        case 0xAA : //Turn Left
          angle[instructCounter] = reading[1]; //add the relative turning angle to instruction set
          if (reading[2] != 0xF0)      //If the stop bit isnt next, something went wrong
          {
            Serial.println("An Error in Communication has occured"); //print error message
          }
          break;
        case 0xBB : //Turn Right
          angle[instructCounter] = reading[1]; //add the turning angle to instruction set
          if (reading[2] != 0xF0)      //If the stop bit isnt next, something went wrong     
          {
            Serial.println("An Error in Communication has occured"); //print error message
          }
          break;            
        case 0xCC : //Go Forward
          distance[instructCounter] = reading[1]; //Add the distance of move to instruction set
          speedy[instructCounter] = reading[2];   //add the speed of move to instruction set
          if (reading[3] != 0xF0)      //If the stop bit isnt next, something went wrong
          {
            Serial.println("An Error in Communication has occured"); //print error message
          }
          break;          
        case 0x00 : //Stop
          Serial.println("Stop!!");
          break;    
        default: //If the action type is not recognized
          Serial.println("Error, Something with wrong with the communication!"); //print error message
          break;      
      }//end switch (between actions)                                 
    }//end if, ending the specific instruction                                
  }// end if reading available
}//end readinstruction function
  

