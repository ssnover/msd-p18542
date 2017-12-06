#!/usr/bin/python3
"""
    file: main.py
    author: Shane Snover
    purpose: Initializes the application and checks arguments for a byte to send.
"""

from sys import argv
import serial

DEVICE_FILEPATH = "/dev/ttyACM0"
my_serial_device = serial.Serial(DEVICE_FILEPATH, 9600, timeout=0)


def wireless_send(byte_to_send):
    """
    Sends a byte over serial.
    :param byte_to_send: A byte as a string '0xNN'. Where N are two hexadecimal
    character.
    :return: Success or failure.
    """

    MESSAGE_ACK = b'\xaa'
    message_ack_status = False

    raw_byte = bytearray.fromhex(byte_to_send.lstrip('0x'))
    if raw_byte == b'':
        raw_byte = b'\x00'
    my_serial_device.write(raw_byte)

    try:
        while not message_ack_status:
            message_ack_status = (my_serial_device.read(1) == MESSAGE_ACK)
    except KeyboardInterrupt:
        print("\rUser ended program.")

    my_serial_device.close()

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
