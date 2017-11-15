#!/usr/bin/python3
"""
    file: unix_socket_server.py
    author: Shane Snover
    purpose: An implementation of a wrapper for the Unix socket API for
             setting up an IPC server.
"""

import os
import socket


class UnixSocketServer:
    """
    A wrapper for Unix sockets implementing a server.
    """
    def __init__(self, socket_path):
        self.socket_path = socket_path
        if os.path.exists(socket_path):
            os.remove(socket_path)
        self.server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    def bind(self):
        self.server.bind(self.socket_path)
        return self

    def receive(self, bytes_to_read):
        return self.server.recv(bytes_to_read).decode('utf-8')

    def close(self):
        self.server.close()

    def cleanup_socket_file(self):
        os.remove(self.socket_path)

    def get_socket_path(self):
        return self.socket_path
