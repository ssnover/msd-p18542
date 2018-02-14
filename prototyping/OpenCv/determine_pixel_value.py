import cv2
import numpy as np
pixel_hsv = []
img = cv2.imread('Hexagon_Terrain_Homography.PNG')
for i in range(0,3):
    for k in range(0,3):

        px = img[140+i,63+k]
        pixel_hsv.insert(i+k, px)
        print(px)

print(np.mean(pixel_hsv, axis = 0))