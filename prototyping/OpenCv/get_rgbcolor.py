
import cv2
import numpy as np
from math import sqrt


def get_rgbcolor(average_hsv):
    distances = []
    gray = "gray"
    blue = "blue"
    green = "green"
    red = "red"
    yellow = "yellow"
    preset_colors = ([127, 127, 127],
                     [204, 72, 63],
                     [76, 177, 34],
                     [36, 28, 237],
                     [0, 242, 255])
    colors = [gray, blue, green, red, yellow]



    for i in range(0,len(preset_colors)):

        dist = sqrt((average_hsv[0]-preset_colors[i][0])**2 +
                    (average_hsv[1]-preset_colors[i][1])**2 +
                    (average_hsv[2]-preset_colors[i][2])**2)
        distances += [dist]
    index_min = np.argmin(distances)

    color = colors[index_min]

    return color
