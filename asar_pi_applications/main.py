#!/usr/bin/python3
"""
    file: main.py
    purpose: Entry point for the ASAR Core application.
"""

from asar_config import ASAR_GLOBALS
from asar_web_server.asar_web_server.asar_web_server import app, get_current_state, get_current_settings, \
    get_most_recent_image
from asar_web_server.asar_web_server.gui_constants import STATE
from asar_comms_server.asar_comms_server import ASARCommunicationsServer
from asar_camera_engine.asar_camera_engine import ASARCameraEngine
from asar_vision.homography_automated import automated_homography
from asar_search_algorithm.A_Star_Search import runSearch


def main():
    """
    Entry point of the application.
    """
    app.run()
    my_camera_engine = ASARCameraEngine(ASAR_GLOBALS.IMAGE_CAPTURE_FREQUENCY_HZ,
                                        ASAR_GLOBALS.DATABASE_PATH,
                                        ASAR_GLOBALS.IMAGE_ROOT_PATH)
    my_camera_engine.begin()
    my_comms_server = ASARCommunicationsServer(ASAR_GLOBALS.SERIAL_PORT_PATH, ASAR_GLOBALS.SERIAL_BAUD_RATE)
    my_comms_server.begin()

    while True:
        my_state = get_current_state()
        if my_state == STATE['STOPPED']:
            pass
        elif my_state == STATE['RUNNING']:
            # get the most recent image
            image = get_most_recent_image()
            terrain_path = automated_homography(image)  # eventually stick this into db
            current_danger_setting, _, _ = get_current_settings()
            robot_directions, coordinates, start_node, end_node = runSearch(terrain_path, current_danger_setting)
            # should save those directions to a file
            my_comms_server.raw_write(robot_directions.decode('ISO-8859-1'))
        elif my_state == STATE['PAUSED']:
            pass
        else:
            pass


if __name__ == "__main__":
    main()
