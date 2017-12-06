#!/usr/bin/python3
"""
    file: main.py
    author: Shane Snover
    purpose: Initializes the application and checks arguments for a byte to send.
"""

from sys import argv
import serial

PI_SERIAL_PATH = "/dev/ttyAMA0"
DEVICE_FILEPATH = "/dev/ttyACM0"


def wireless_send(byte_to_send, port):
    """
    Sends a byte over serial.
    :param byte_to_send: A byte as a string '0xNN'. Where N are two hexadecimal
    character.
    :param port: The filepath for the serial port connection.
    :return: Success or failure.
    """
    my_serial_device = serial.Serial(port, 9600, timeout=0)
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
    port = DEVICE_FILEPATH
    if 'p' in my_arguments and my_arguments['p'] == 'pi':
        port = PI_SERIAL_PATH
    send_status = wireless_send(my_arguments['b'], port)
    print("Message Status: ", end='')
    print(send_status)
    return


if __name__ == "__main__":
    main()
