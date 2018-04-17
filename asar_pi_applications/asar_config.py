"""
    file: asar_config.py
    purpose: A group of constants used throughout the ASAR applications.
"""

import os


class ASAR_GLOBALS(object):
    """
    An aggregate of all the global variables for configuration.
    """

    DATABASE_PATH = os.path.join(os.sep, 'home', 'pi', 'asar', 'db')
    IMAGE_CAPTURE_FREQUENCY_HZ = 2
    IMAGE_ROOT_PATH = os.path.join(os.sep, 'home', 'pi', 'asar', 'images')
    SERIAL_PORT_PATH = os.path.join(os.sep, 'dev', 'serial0')
    SERIAL_BAUD_RATE = 115200
