
import cv2
import numpy as np
from math import sqrt
import json


def get_rgbcolor(average_hsv):
    distances = []
    red = "red"
    blue = "blu"
    green = "grn"
    gray = "gry"
    purple = "prp"
    yellow = "yel"
    orange = "org"
    pink = "pnk"
    black = "blk"
    colors = [red, blue, green, gray, purple, yellow, orange, pink, black]
    parameters = json.load(open('parameters.txt'))
    if len(parameters['value']) < 9:
        preset_colors = ([36, 28, 237],
                         [204, 72, 63],
                         [76, 177, 34],
                         [127, 127, 127],
                         [164, 73, 163],
                         [0, 242, 255],
                         [39, 127, 255],
                         [255, 0, 255],
                         [0, 0, 0])
        for i in range(0, len(preset_colors)):
            dist = sqrt((average_hsv[0] - preset_colors[i][0]) ** 2 +
                        (average_hsv[1] - preset_colors[i][1]) ** 2 +
                        (average_hsv[2] - preset_colors[i][2]) ** 2)
            distances += [dist]
        index_min = np.argmin(distances)

    else:
        preset_colors = ([parameters['value'][0][0]],
                         [parameters['value'][0][1]],
                         [parameters['value'][0][2]],
                         [parameters['value'][0][3]],
                         [parameters['value'][0][4]],
                         [parameters['value'][0][5]],
                         [parameters['value'][0][6]],
                         [parameters['value'][0][7]],
                         [parameters['value'][0][8]])


        for i in range(0, len(preset_colors)):

            dist = sqrt((average_hsv[0]-preset_colors[i][0][0])**2 +
                        (average_hsv[1]-preset_colors[i][0][1])**2 +
                        (average_hsv[2]-preset_colors[i][0][2])**2)
            distances += [dist]
        index_min = np.argmin(distances)

    color = colors[index_min]
    print(preset_colors[index_min])
    print(color)
    return color
