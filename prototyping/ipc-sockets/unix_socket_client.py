#!/usr/bin/python3
"""
    file: unix_socket_client.py
    author: Shane Snover
    purpose: A wrapper for the Python API to the Unix socket for clients.
"""

import socket


class UnixSocketClient:
    """
    Object for interfacing with a Unix socket server.
    """

    def __init__(self, socket_path):
        self.socket_path = socket_path
        self.client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    def connect(self):
        self.client.connect(self.socket_path)
        return self

    def transmit(self, str_to_transmit):
        self.client.send(str_to_transmit.encode('utf-8'))
        return

    def close(self):
        self.client.close()

    def get_socket_path(self):
        return self.socket_path
