/*
 * file: command-manager.h
 * purpose: Interface definition for the command manager application.
 */

#ifndef COMMAND_MANAGER_H
#define COMMAND_MANAGER_H


#include <array>
#include "command.h"

namespace ASAR
{

class COMMAND_MANAGER
{
private:

   enum class STATE
   {
      // different states for the command manager application
   };

   STATE my_current_state;
   STATE my_next_state;
   bool my_state_changed;
   std::array<COMMAND_INTF> my_command_queue;

   void enterState();
   void processState();
   void exitState();

public:

   COMMAND_MANAGER();
   ~COMMAND_MANAGER();

   void run();

   COMMAND_INTF & const getNextCommand();


};

}

#endif   // COMMAND_MANAGER_H