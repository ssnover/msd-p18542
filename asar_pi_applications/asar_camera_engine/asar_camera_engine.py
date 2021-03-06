#!/usr/bin/python3
"""
    file: asar-camera-engine.py
    purpose: Specifies the class for controlling and interfacing to the Raspberry Pi Camera.
"""

import datetime
import os
import sqlite3
import threading
import time


try:
    from picamera import PiCamera
except ImportError:
    print("PiCamera module is not installed.")
    quit()


class ASARCameraEngine:

    def __init__(self, frequency, database_store_call, image_path):
        """
        Constructor.
        """
        self.my_camera = PiCamera()
        self.my_capture_call = database_store_call
        self.my_images_directory = image_path
        self.my_capture_frequency = frequency
        self.my_worker_thread = threading.Thread(target=self.cameraEngineImageContext, args=())
        self.my_worker_thread.daemon = True
        self.my_running_status = False
        self.my_camera_is_busy = False

    def begin(self):
        """
        Start the thread controlling the ASAR camera engine.
        :return: Boolean representing the running state of the camera engine.
        """
        if self.my_camera_is_busy:
            return False
        self.my_running_status = True
        self.my_worker_thread.start()
        return True

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
        dt_string = '{:04d}'.format(current_time.year) \
                  + '{:02d}'.format(current_time.month) \
                  + '{:02d}'.format(current_time.day) \
                  + '_' \
                  + '{:02d}'.format(current_time.hour) \
                  + '{:02d}'.format(current_time.minute) \
                  + '{:02d}'.format(current_time.second) \
                  + '_' \
                  + '{:06d}'.format(current_time.microsecond)
        filename = dt_string + '.jpg'
        image_path = os.path.join(self.my_images_directory, filename)

        self.my_camera.capture(image_path, use_video_port=True)

        return image_path

    def takeVideo(self, path, length_in_seconds):
        """
        Requests the engine to take a video.
        :param path: The absolute path to the video file to create.
        :param length_in_seconds: Length of video to record in seconds.
        :return: Boolean of whether capture was started.
        """
        if path.split('.')[-1] != 'h264':
            return False
        if self.my_running_status:
            return False

        video_thread = threading.Thread(target=self.cameraEngineVideoContext,
                                        args=(path, length_in_seconds))
        video_thread.start()
        return True

    def cameraEngineImageContext(self):
        """
        Executed by the camera engine application to take a picture on a set rate.
        :return: None.
        """
        while self.my_running_status:
            print("Taking that picture!")
            # need to start putting image paths in database
            new_image_path = self.takePicture()

            time.sleep(1 / self.my_capture_frequency - 0.1)

    def cameraEngineVideoContext(self, path, length_in_seconds):
        """
        Executed by the camera engine application to take a video for a set
        amount of time.
        :param path: Path to store the video capture at.
        :param length_in_seconds:
        :return: None
        """
        self.my_camera_is_busy = True
        start_time = datetime.datetime.now()
        self.my_camera.start_recording(path)

        while (datetime.datetime.now() - start_time).seconds < length_in_seconds:
            pass

        self.my_camera.stop_recording()
        self.my_camera_is_busy = False


def main():
    """
    Entry point for testing.
    :return:
    """
    TOTAL_TIME_TO_RUN_SECONDS = 10
    CAPTURE_FREQUENCY_HZ = 2
    IMAGE_STORAGE_LOCATION = os.path.join(os.sep, 'home', 'pi', 'asar', 'images')

    my_camera = ASARCameraEngine(CAPTURE_FREQUENCY_HZ,
                                 os.path.join(os.sep, 'tmp', 'asar.db'),
                                 IMAGE_STORAGE_LOCATION)
    my_camera.begin()
    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < TOTAL_TIME_TO_RUN_SECONDS:
        time.sleep(1)

    my_camera.end()

    for filename in os.listdir(IMAGE_STORAGE_LOCATION):
        if '.jpg' in filename:
            os.remove(os.path.join(IMAGE_STORAGE_LOCATION, filename))

    return 0


if __name__ == "__main__":
    main()
