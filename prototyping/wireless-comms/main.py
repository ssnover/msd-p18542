#!/usr/bin/python3
"""
    file: main.py
    author: Shane Snover
    purpose: Initializes the application and listens for packets.
"""

from sys import argv
import serial


def wireless_send(byte_to_send):
    """
    Sends a byte over serial.
    :param byte_to_send: A byte as a string '0xNN'. Where N are two hexadecimal
    character.
    :return: Success or failure.
    """

    message_ack_status = False

    return message_ack_status


def getopts(argument_list):
    """
    Parses command line arguments from argv.
    :param argument_list: The command line input from the terminal, separated as a list.
    :return: Dictionary of argument name to value.
    """

    opts = {}
    while argument_list:
        if argument_list[0][0] == '-':
            opts[argument_list[0].lstrip('-')] = argument_list[1]
        argument_list = argument_list[1:]
    return opts


def main():
    """
    Entry point of the application.
    :return: None.
    """

    my_arguments = getopts(argv)
    # open the serial port
    print(my_arguments)
    send_status = wireless_send(my_arguments['b'])
    print("Message Status: ", end='')
    print(send_status)
    return


if __name__ == "__main__":
    main()
