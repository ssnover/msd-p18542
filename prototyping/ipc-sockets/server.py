#!/usr/bin/python3
"""
    file: server.py
    author: Shane Snover
    purpose: A small script to spin up an IPC server to demonstrate controlling
             the transfer of data between Python applications via Unix sockets.
"""

from prototype_globals import SOCKET_PATH
from unix_socket_server import UnixSocketServer


def main():
    """
    Entry point of the application.
    :return: None
    """
    my_ipc_server = UnixSocketServer(SOCKET_PATH)
    my_ipc_server.bind()
    print("IPC Server is listening for incoming traffic.")

    try:
        while True:
            sent_string = my_ipc_server.receive(100)
            print(sent_string)
    except KeyboardInterrupt:
        print("Shutting down the IPC server.")
        my_ipc_server.close()
        my_ipc_server.cleanup_socket_file()


if __name__ == "__main__":
    main()
