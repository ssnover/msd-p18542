/*
 * file: asar.ino
 * purpose: Entry point for the execution of ASAR robot firmware.
 */

#include <stdbool.h>
#include "Arduino.h"


void setup()
{
	// This function is serving as our main function. Do not return.

	// Initialization of drivers
	// Loop forever
	while (true)
	{
		asm volatile(" nop\r\n");
	}
}


void loop()
{
	// This function should remain empty.
	while (true)
	{
		asm volatile(" nop\r\n");
	}
}