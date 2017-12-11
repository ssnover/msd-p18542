/*
 * file: command-manager.cpp
 * purpose: Reads commands transmitted by the Aerial Platform and parses them
 *          as Command objects.
 */

#include "aerial-platform.h"
#include "command-manager.h"

namespace ASAR
{

COMMAND_MANAGER::COMMAND_MANAGER()
{
   // constructor
}


COMMAND_MANGER::~COMMAND_MANAGER()
{
   // destructor
}


COMMAND_MANAGER::run()
{
   if (this->my_state_changed)
   {
      this->enterState();
   }

   this->processState();

   if (this->my_current_state != this->my_next_state)
   {
      this->exitState();
      this->my_state_changed;
      this->my_current_state = this->my_next_state;
   }
}


COMMAND_MANAGER::enterState()
{

}

}