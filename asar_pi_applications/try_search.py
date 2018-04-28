#!/usr/bin/python3
"""
    file: main.py
    purpose: Entry point for the ASAR Core application.
"""

from asar_config import ASAR_GLOBALS
from asar_comms_server.asar_comms_server import ASARCommunicationsServer
from asar_search_algorithm.A_Star_Search import runSearch


def main():
    """
    Entry point of the application.
    """
    my_comms_server = ASARCommunicationsServer(ASAR_GLOBALS.SERIAL_PORT_PATH, ASAR_GLOBALS.SERIAL_BAUD_RATE)
    my_comms_server.begin()
    terrain_path = "borked_out.txt"
    current_danger_setting = 3 
    # get the most recent image
    robot_directions, coordinates, start_node, end_node = runSearch(terrain_path, current_danger_setting)
    # should save those directions to a file
    print(robot_directions)
    for coordinate in coordinates:
        print(coordinate)

    my_comms_server.raw_write(robot_directions)
    my_comms_server.end()


if __name__ == "__main__":
    main()
