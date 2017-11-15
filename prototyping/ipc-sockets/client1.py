#!/usr/bin/python3
"""
    file: client1.py
    author: Shane Snover
    purpose: A small script for spinning up an IPC client to demonstrate how
             information can be communicated via Linux sockets in Python.
"""

from prototype_globals import SOCKET_PATH
from unix_socket_client import UnixSocketClient


def main():
    """
    The entry point of the application.
    :return: None
    """
    my_ipc_client = UnixSocketClient(SOCKET_PATH)
    my_ipc_client.connect()
    print("Socket is connected to server.")
    print("Press Ctrl+C to quit.")

    while True:
        try:
            text_to_send = input("> ")
            my_ipc_client.transmit(text_to_send)
        except KeyboardInterrupt:
            print("Closing IPC client.")
            my_ipc_client.close()
            break


if __name__ == "__main__":
    main()
