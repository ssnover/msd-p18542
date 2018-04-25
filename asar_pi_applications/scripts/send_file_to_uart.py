#!/usr/bin/python3

import os
import sys
# add the top level path to the interpreter search path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path)

from asar_comms_server.asar_comms_server import ASARCommunicationsServer

def main():
    """
    Sends a string of bytes in a file to a device over UART.
    """
    my_comms_server = ASARCommunicationsServer("/dev/serial0", 9600)
    my_comms_server.begin()

    my_file = open("demo_instructions.bin", 'r')
    my_instructions = my_file.read()
    my_encoded_instructions = my_instructions.encode('ISO-8859-1')
    print(my_instructions)
    print(my_encoded_instructions)
    my_comms_server.write(my_instructions)


if __name__ == "__main__":
    main()
