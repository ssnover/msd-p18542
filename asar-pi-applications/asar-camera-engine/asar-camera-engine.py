#!/usr/bin/python3
"""
    file: asar-camera-engine.py
    purpose: Specifies the class for controlling and interfacing to the Raspberry Pi Camera.
"""

import datetime as dt
import os

try:
    from picamera import PiCamera
except ImportError:
    print("PiCamera module is not installed.")
    quit()


class ASARCameraEngine:

    def __init__(self):
        """
        Constructor.
        """
        self.my_camera = PiCamera()
        self.my_images_directory = os.path.join(os.sep, 'home', 'pi', 'asar', 'images')

    def run(self):
        """
        Start the thread controlling the ASAR camera engine.
        :return: None.
        """
        pass

    def stop(self):
        """
        Stop the ASAR camera engine execution.
        :return: None.
        """
        pass

    def takePicture(self):
        """
        Requests the engine to take a picture with the PiCamera.
        :return: Path to the image.
        """
        current_time = dt.datetime.now()
        dt_string = str(current_time.year) + str(current_time.month) + str(current_time.day) + '_' + str(
            current_time.hour) + str(current_time.minute) + str(current_time.second)
        image_path = dt_string + '.jpg'
        self.my_camera.capture(image_path)
        return image_path
