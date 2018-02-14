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


class ASARCommunicationsServer:
    """
        Class
    """

    def __init__(self, driver_path, baud_rate=9600):
        self.my_driver_path = driver_path
        self.my_baud_rate = baud_rate
        self.my_handlers = {}
        self.my_server_is_running = False
        self.my_serial_port = None
        self.my_message_termination = bytes('\n', encoding='utf-8')
        self.my_received_message_buffer = []
        self.my_receive_worker_thread = None
        return

    def begin(self):
        """
        Initializes and the server for full duplex communication.
        """
        # Create the serial port object
        self.my_serial_port = serial.Serial(self.my_driver_path,
                                            self.my_baud_rate,
                                            parity=serial.PARITY_NONE,
                                            bytesize=serial.EIGHTBITS,
                                            timeout=1)
        self.my_serial_port.reset_input_buffer()
        self.my_serial_port.open()
        # Internal bookkeeping to mark the server is running
        self.my_server_is_running = True
        # Spin up a new thread to run the server
        self.my_receive_worker_thread = threading.Thread(target=self.server_context,
                                                         name="ASAR Comms Server Thread").start()
        return

    def end(self):
        """
        Closes the communications server.
        """
        self.my_receive_worker_thread.stop()
        self.my_server_is_running = False
        self.my_serial_port.close()
        return

    def write(self, message_to_transmit):
        """
        Sends a string of bytes over the communications server.
        """
        self.my_serial_port.write(message_to_transmit, encoding='utf-8')
        return

    def read(self):
        """
        Reads a message from the buffer.
        """
        return self.my_received_message_buffer.pop(0)

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
        message_in_progress = []

        while self.my_server_is_running:
            new_byte = self.my_serial_port.read(1)
            if new_byte is not b'':
                message_in_progress += [new_byte]
            if new_byte is self.my_message_termination:
                # full new message has been received
                # add to the buffer, make a deep copy
                self.my_received_message_buffer += [message_in_progress[:]]
                # call the callbacks
                for callback in self.my_handlers:
                    callback()
                # then empty our local buffer
                message_in_progress = []


def main():
    """
    Run a series of tests or an individual test.
    """
    TOTAL_TIME_TO_RUN = 60
    message_dump_file = os.path.join("", "tmp", "comms_received.txt")
    my_comms_server = ASARCommunicationsServer("/dev/ttyACM0", 9600)
    my_comms_server.begin()

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < TOTAL_TIME_TO_RUN:
        if my_comms_server.messages_received():
            while my_comms_server.messages_received():
                file = open(message_dump_file, 'w')
                file.write(my_comms_server.read() + '\n')
                file.close()
            my_comms_server.write("I'm listening...")
        else:
            my_comms_server.write("I'm talking...")
        sleep(1)


if __name__ == "__main__":
    main()
