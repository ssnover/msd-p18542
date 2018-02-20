#!/usr/bin/python3
"""
    file: asar_comms_server.py
    purpose: Entry point for Communications server testing and definition of
             the communications server class.
"""

import datetime
import os
import serial
import threading
from time import sleep


class ASARCommunicationsServer(object):
    """
    Object for interfacing with the robot over XBee UART radios.

    This class abstracts the encoding and handling of messages such that the
    application can easily read new messages that have already been parsed and
    decoded and send messages without worrying about the required encoding.
    """

    def __init__(self, driver_path, baud_rate=9600):
        """
        Constructs the communication server.
        :param driver_path: The path to the USB port driver file.
        :param baud_rate: The baud rate of the UART communication.
        """
        self.my_driver_path = driver_path
        self.my_baud_rate = baud_rate
        self.my_handlers = {}
        self.my_server_is_running = False
        self.my_serial_port = serial.Serial(self.my_driver_path,
                                            self.my_baud_rate,
                                            parity=serial.PARITY_NONE,
                                            bytesize=serial.EIGHTBITS,
                                            timeout=1)
        self.my_message_termination_char = '\n'
        self.my_received_message_buffer = []
        self.my_receive_worker_thread = threading.Thread(target=self.server_context,
                                                         args=(),
                                                         name="ASAR Comms Server Thread")

    def begin(self):
        """
        Initializes and the server for full duplex communication.

        :return Success of the call to begin.
        """
        # Create the serial port object
        if self.my_server_is_running:
            # Already running
            return False

        self.my_serial_port.reset_input_buffer()

        # check that another program is not using the serial port
        print("Opening the serial port")
        # Internal bookkeeping to mark the server is running
        self.my_server_is_running = True
        # Spin up a new thread to run the server
        self.my_receive_worker_thread.start()

        return self.my_server_is_running

    def end(self):
        """
        Closes the communications server.
        """
        self.my_server_is_running = False
        #self.my_receive_worker_thread.join()
        self.my_serial_port.close()
        return

    def write(self, message_to_transmit):
        """
        Sends a string of bytes over the communications server.
        """
        if self.my_server_is_running:
            print("Transmit away!")
            self.my_serial_port.write((message_to_transmit + self.my_message_termination_char).encode('utf-8'))
            return True
        else:
            return False

    def read(self):
        """
        Reads a message from the buffer.
        """
        if self.messages_received() > 0:
            return self.my_received_message_buffer.pop(0)
        else:
            return ""

    def messages_received(self):
        """
        Returns the number of messages in the buffer.
        :return:
        """
        return len(self.my_received_message_buffer)

    def server_context(self):
        """
        A method to be run in a separate thread to handle messages as they're received.
        :return:
        """
        message_in_progress = ""

        while self.my_server_is_running:
            new_byte = self.my_serial_port.read(1).decode('utf-8')
            if new_byte is not '':
                # empty string indicates a timeout
                message_in_progress += new_byte
            if new_byte is self.my_message_termination_char:
                # full new message has been received
                # add to the buffer, make a deep copy
                self.my_received_message_buffer += [message_in_progress[:]]
                print(message_in_progress)
                # call the callbacks
                for callback in self.my_handlers:
                    callback()
                # then empty our local buffer
                message_in_progress = ""


def main():
    """
    Run a series of tests or an individual test.
    """
    TOTAL_TIME_TO_RUN = 10
    message_dump_file = os.path.join(os.sep, "tmp", "comms_received.txt")
    my_comms_server = ASARCommunicationsServer("/dev/serial0", 9600)
    my_comms_server.begin()

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < TOTAL_TIME_TO_RUN:
        if my_comms_server.messages_received():
            while my_comms_server.messages_received():
                file = open(message_dump_file, 'a')
                file.write(my_comms_server.read() + '\n')
                file.close()
            print("I'm listening...")
            my_comms_server.write("I'm listening...")
        else:
            print("I'm talking...")
            my_comms_server.write("I'm talking...\n")
        sleep(1)

    my_comms_server.end()


if __name__ == "__main__":
    main()
