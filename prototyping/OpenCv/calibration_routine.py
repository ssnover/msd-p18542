import sys
import numpy as np
import cv2
from utils import get_four_points
upper_bound = []
lower_bound = []
rgb_color = []


im = cv2.imread('hex_t.PNG')
print('First start by clicking on a red tile\n')
print('proceed to click on a blue tile\n then green...purple\n yellow\n orange\n black')

points = get_four_points(im)

'''   
blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]
'''
for i in range(0, len(points)):

    color_point_x = np.int64(points[i][0])
    color_point_y = np.int64(points[i][1])


    rgb_color.append(im[color_point_x, color_point_y])
for i in range(0, len(rgb_color)):
    blue = rgb_color[i][0]
    green = rgb_color[i][1]
    red = rgb_color[i][2]
    color = np.uint8([[[blue, green, red]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]

    lower_bound += [hue - 10, 100, 100]
    upper_bound += [hue + 10, 255, 255]

print(upper_bound)
print(lower_bound)

