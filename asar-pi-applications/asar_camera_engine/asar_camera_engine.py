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


class CameraEngineContextThread(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self)
        self.my_target = target
        self.daemon = True

    def run(self):
        self.my_target()


class ASARCameraEngine:

    def __init__(self, frequency, database_path):
        """
        Constructor.
        """
        self.my_camera = PiCamera()
        self.my_database_path = database_path
        self.my_images_directory = os.path.join(os.sep, 'home', 'pi', 'asar', 'images')
        self.my_capture_frequency = frequency
        print(1 / self.my_capture_frequency)
        #self.my_worker_thread = CameraEngineContextThread(self.camera_engine_context)
        self.my_worker_thread = threading.Thread(target=self.camera_engine_context, args=())
        self.my_worker_thread.daemon = True
        self.my_running_status = False

    def begin(self):
        """
        Start the thread controlling the ASAR camera engine.
        :return: None.
        """
        self.my_running_status = True
        self.my_worker_thread.start()
        print("Starting up the thread for taking pictures.")
        #self.my_running_status = True

    def end(self):
        """
        Stop the ASAR camera engine execution.
        :return: None.
        """
        print("Shutting down camera engine")
        self.my_running_status = False
        self.my_worker_thread.join()

    def takePicture(self):
        """
        Requests the engine to take a picture with the PiCamera.
        :return: Path to the image.
        """
        current_time = datetime.datetime.now()
        dt_string = str(current_time.year) + str(current_time.month) + str(current_time.day) + '_' + str(
            current_time.hour) + str(current_time.minute) + str(current_time.second)
        image_path = dt_string + '.jpg'
        image_path = os.path.join(self.my_images_directory, image_path)
        print("New image: " + image_path)
        time_start = datetime.datetime.now()
        self.my_camera.capture(image_path)
        time_end = datetime.datetime.now()

        print((time_end - time_start).microseconds)

        return image_path

    def camera_engine_context(self):
        """
        Executed by the camera engine thread to take a picture on a set rate.
        :return:
        """
        print("Entered the camera engine context.")
        self.my_camera.start_recording(os.path.join(self.my_images_directory, 'video.h264'))

        while self.my_running_status:
            print("Taking that picture!")
            #self.takePicture()
            time.sleep(1 / self.my_capture_frequency)

        self.my_camera.stop_recording()


def main():
    """
    Entry point for testing.
    :return:
    """
    TOTAL_TIME_TO_RUN_SECONDS = 10
    CAPTURE_FREQUENCY_HZ = 2

    my_camera = ASARCameraEngine(CAPTURE_FREQUENCY_HZ, os.path.join(os.sep, 'tmp', 'asar.db'))
    my_camera.begin()

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < TOTAL_TIME_TO_RUN_SECONDS:
        time.sleep(1)

    my_camera.end()


if __name__ == "__main__":
    main()
