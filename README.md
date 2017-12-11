# msd-p18542
Repository for RIT MSD P18542 source code, schematics, and CAD models.

# P18452: Real Time Terrain Mapping
In search and rescue operations time is often of the essence and the terrain can end up being wildly different than expected. The ability to image a landscape and use this data to determine the quickest route for operatives driving vehicles in this changing terrain in real-time could save lives in these scenarios. The goal of this project is to lay groundwork on this idea by imaging an area in real-time and using the image to plot route for a small autonomous vehicle.

## ASAR Robot
The first portion of this project consists of the electrical and PCB schematics for the robot along with mechanical CAD drawings and firmware for the Teensy 3.2 microcontroller development board.

### ASAR Teensy Firmware
The source code for the applications running on the Teensy is written for C++11 and will be made up of three primary applications run on a system tick:
1. Search and Rescue - controls search for the survivor and collection of data
2. Locomotion - controls movement of the robot
3. Command Manager - interfaces to the ASAR Aerial Platform to receive commands

## ASAR Aerial Platform
The second major portion of the project is a series of Python 3 modules run on a Raspberry Pi 3. These present a GUI for running the simulation and algorithms related to the computer vision and path finding aspects of the project. The major components include:
1. asar-camera-engine - Interface to the Raspberry Pi Camera
2. asar-vision - Generates a terrain map model from images
3. asar-path-finder - Takes the map model and finds the quickest path between two points
4. asar-web-ui - A web app hosted on the Pi to act as a GUI
5. asar-comms-server - Interface to the Pi's hardware UART
6. asar-core - The application the controls the flow of data between all of the above 