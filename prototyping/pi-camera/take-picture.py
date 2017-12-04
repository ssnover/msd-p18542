#!/usr/bin/python3
"""
    file: take-picture.py
    author: Shane Snover
    purpose: This is a small script to test the most basic function of the
             Raspberry Pi camera API in Python; taking a picture and saving it
             to the filesystem.
"""


import os
from picamera import PiCamera


def main():
    """
    The entry point of the application.
    :return: None
    """
    my_camera = PiCamera()
    image_path = os.path.join(os.sep, 'home', 'pi', 'asar', 'images', 'prototyping-image.jpg')

    my_camera.capture(image_path)


if __name__ == "__main__":
    main()
