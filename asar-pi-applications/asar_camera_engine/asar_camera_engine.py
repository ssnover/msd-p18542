#!/usr/bin/python3
"""
    file: asar-camera-engine.py
    purpose: Specifies the class for controlling and interfacing to the Raspberry Pi Camera.
"""

import datetime
import os
import threading
import time

try:
    from picamera import PiCamera
except ImportError:
    print("PiCamera module is not installed.")
    quit()


class ASARCameraEngine:

    def __init__(self, frequency):
        """
        Constructor.
        """
        self.my_camera = PiCamera()
        self.my_images_directory = os.path.join(os.sep, 'home', 'pi', 'asar', 'images')
        self.my_capture_frequency = frequency
        self.my_worker_thread = threading.Thread(target=self.camera_engine_context,
                                                 name="ASAR Camera Engine Worker Thread")
        self.my_running_status = False

    def begin(self):
        """
        Start the thread controlling the ASAR camera engine.
        :return: None.
        """
        self.my_worker_thread.start()
        self.my_running_status = True

    def end(self):
        """
        Stop the ASAR camera engine execution.
        :return: None.
        """
        self.my_worker_thread.stop()
        self.my_running_status = False

    def takePicture(self):
        """
        Requests the engine to take a picture with the PiCamera.
        :return: Path to the image.
        """
        current_time = datetime.datetime.now()
        dt_string = str(current_time.year) + str(current_time.month) + str(current_time.day) + '_' + str(
            current_time.hour) + str(current_time.minute) + str(current_time.second)
        image_path = dt_string + '.jpg'

        self.my_camera.capture(image_path)

        return image_path

    def camera_engine_context(self):
        """
        Executed by the camera engine thread to take a picture on a set rate.
        :return:
        """
        while True:
            self.takePicture()
            time.sleep(1 / self.my_capture_frequency)


def main():
    """
    Entry point for testing.
    :return:
    """
    TOTAL_TIME_TO_RUN_SECONDS = 60
    my_camera = ASARCameraEngine(2)
    my_camera.begin()

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < TOTAL_TIME_TO_RUN_SECONDS:
        time.sleep(1)


if __name__ == "__main__":
    main()
