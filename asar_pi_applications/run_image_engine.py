#!/usr/bin/python3
"""
    file: run_image_engine.py
    purpose: Takes a picture with the PiCamera and runs the vision software
             in order to generate a map which is printed to the user.
"""

import os
from asar_vision.homography_automated import automated_homography
from asar_camera_engine.asar_camera_engine import ASARCameraEngine


def imaging_test():
    """
    Takes a picture with the PiCamera and runs the vision software
    in order to generate a map which is printed to the user.
    """

    #my_camera = ASARCameraEngine(1,
    #                             os.path.join(os.sep, 'home', 'pi', 'asar', 'database'),
    #                             os.path.join(os.sep, 'home', 'pi', 'asar', 'images'))
    image_path = "/home/pi/asar/images/prototyping-image.jpg" # my_camera.take_picture()
    terrain_path = automated_homography(image_path)
    terrain_file = open(terrain_path, 'r')
    print(terrain_file.read())
    terrain_file.close()
    return


if __name__ == "__main__":
    imaging_test()
