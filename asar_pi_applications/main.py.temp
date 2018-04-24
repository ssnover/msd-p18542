#!/usr/bin/python3
"""
    file: main.py
    purpose: Entry point for the ASAR Core application.
"""
from asar_web_server.asar_web_server.asar_web_server import app
from asar_comms_server.asar_comms_server import ASARCommunicationsServer
from asar_camera_engine.asar_camera_engine import ASARCameraEngine
# vision
# pathfinding


def main():
    """
    Entry point of the application.
    """
    app.run()
    my_camera_engine = ASARCameraEngine(2, ASAR_DATABASE_PATH, IMAGE_ROOT_PATH)
    my_camera_engine.begin()
    my_comms_server = ASARCommunicationsServer(ASAR_SERIAL_PORT_PATH, ASAR_BAUD_RATE)
    my_comms_server.begin()

    # while true
        # while running
            # take pictures
            # give the picture to vision
            # take the file from vision and give it to path-finder
            # take the coordinate list and turn into bytecode
            # if different from last one
                # give 


if __name__ == "__main__":
    main()
