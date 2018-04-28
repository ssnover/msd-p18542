import numpy as np
from math import sqrt

def robot_distance_incorrect(robot_actual_location, hexagon_pixel_values):
    distance_to_get_back = []
    distances = []
    pixel_distance = []

    for i in range(0, len(hexagon_pixel_values)):
        dist = sqrt((robot_actual_location[0] - hexagon_pixel_values[i][0]) ** 2 +
                    (robot_actual_location[1] - hexagon_pixel_values[i][1]) ** 2)
        distances += [dist]
    index_min = np.argmin(distances)
    correct_position = hexagon_pixel_values[index_min]
    # find the distance that needs to be traveled to get to the correct location
    pixel_distance = (correct_position[0] - robot_actual_location[0], correct_position[1]-robot_actual_location[1])
    # print(correct_position, robot_actual_location, pixel_distance)
    # convert to actual distance
    distance_to_get_back = (pixel_distance[0]/1.79, pixel_distance[1]/1.749)
    return distance_to_get_back
