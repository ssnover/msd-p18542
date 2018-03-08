
#include "PITimer.h"
#include "Wire.h"

auto XBEE = Serial1;

const int LED = 13;             //Debug LED
bool Flag = false;              //Flag to start loop
const double sPeriod = .001;      //Period at which loop runs

int instructNum = 1;            //couner for instruction number initialized to one
int rawRead[5] = {0};           //temporary hold place from direct reading of xbee

/*Set of arrays that include all the instrctions  *
 *(index of array is instruction number           */
int action[20] = {0x00};
int distance[20] ={0x00};
int angle[20] = {0x00};
int speedy[20] = {0x00};

/*Function Declerations*/
void callback();           //Interrupt function starting the loop
void readRawInstruct();    //Function that reads xbee and updates insruction variables
void Interpret_instruct(); //Interprets a single instruction and fills global instructions
void printInstructSet();   //prints all of the instructions
void GetInstructions(int expectedNumInstructions);

void setup()
{
  Serial.begin(115200);     //Initialize Serial Monitor w/ baud rate
  XBEE.begin(115200);       //Initialize Xbee, with baud rate
  pinMode(LED, OUTPUT);     //Initialize LED as output
  PITimer1.period(sPeriod); //Initialize timer1
  PITimer1.start(callback); //attaches callback() as a timer overflow interrupt
}

void loop()
{
  while (Flag)    //Run the loop only when flag (from callback) is raised
  {
    Flag = false;              //lower the flag so loop doesnt run again until time
    GetInstructions(5);
  }
}

/*callback function is interrupt function that tells the loop when it is time to run. *
* It gets called every sPeriod Seconds                                                */
void callback()                                     
{
  digitalWrite(LED, digitalRead(13) ^ 1); //toggle LED
  Flag = true;                            //Raise Flag
}

/*Read a single Instruction from xbee*/
void readRawInstruct()
{
  if (XBEE.available() && XBEE.read() == 0xFF)               //Only if there is something from xbee to read
  {
    for (int i = 0; i <= 5; i++)        //Read all the inputs (until stop bit is read)
    {
      rawRead[i] = XBEE.read();             //and fill up the temporary array
      //Serial.print("Argument # "); Serial.print(i);
      //Serial.print(", Raw reading: "); Serial.println(rawRead[i], HEX); 
      if(rawRead[i] == 0xF0)
      {
        i = 6;
      }
      else if (i >= 4)
      {
        Serial.println("ERROR-001: Stop Bit Not Detected");
      }
    }
  }                                   
}

/*Interprets a single raw reading instruction, fills relevant arrays 
 * with the index being the number of instruction */
void Interpret_instruct()
{
  action[instructNum] = rawRead[0]; //add the action to instruction set
  switch (action[instructNum])      //switch between the different types of moves
  {
    case 0xAA : //Turn Left
      angle[instructNum] = rawRead[1]; //add the relative turning angle to instruction set
      if (rawRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong
      {
        Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
      }
      break;
    case 0xBB : //Turn Right
      angle[instructNum] = rawRead[1]; //add the turning angle to instruction set
      if (rawRead[2] != 0xF0)          //If the stop bit isnt next, something went wrong     
      {
        Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
      }
      break;            
    case 0xCC : //Go Forward
      distance[instructNum] = rawRead[1]; //Add the distance of move to instruction set
      speedy[instructNum] = rawRead[2];   //add the speed of move to instruction set
      if (rawRead[3] != 0xF0)             //If the stop bit isnt next, something went wrong
      {
        Serial.println("ERROR-002: Stop Bit Not Detected as expected"); //print error message
      }
      break;           
    default: //If the action type is not recognized
      Serial.println("ERROR-003: Move-type not not recognized"); //print error message
      break;  
  }
  for (int i = 0; i < 5; i++) 
  {
    rawRead[i] = 0;
  }
}


/* Function that prints full instruction set */
void printInstructSet()
{
  for (int i = 1; i <= instructNum; i++) //For each instruction
  {
    Serial.print("Instruction: "); Serial.println(i);
    switch (action[i])      //switch between the different types of moves
    {
      case 0xAA : //Turn Left
        Serial.println("  Move Type: Left Turn");
        Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
        break;
      case 0xBB : //Turn Right
        Serial.println("  Move Type: Right Turn");
        Serial.print("    Angle: "); Serial.print(angle[i]); Serial.println (" degrees");
        break;
      case 0xCC : //Forwarmd
        Serial.println("  Move Type: Forward");
        Serial.print("    Distance: "); Serial.println(distance[i]);
        Serial.print("    Speed: "); Serial.println(speedy[i]);
        break;
      default :
        Serial.println("ERROR-003: Move-type not not recognized");
    }
  }
}

/*Main loop reads xbee data, interpretes it as instucionts and prints them on motior*/
void GetInstructions(int expectedNumInstructions)
{
  readRawInstruct();         //reads a single instruction set from the XBEE
  if (rawRead[0] != 0)       // If an instruction was actually read
  {
    Interpret_instruct();   //Function call that interprets the latest instruction and fills global arrays      
    if (instructNum >= expectedNumInstructions) //If last instuction was read and intepretted
    {
      printInstructSet();   //Prints the entire instruction set
      instructNum = 1;      //reset the instruction counter
    }
    else                    //Otherwise (not the last instruction)
    {
      instructNum ++;       //Increment the instruction counter
    }
  }
}

