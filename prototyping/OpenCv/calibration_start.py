import cv2
import numpy as np
from four_corners import four_points
from get_attributes import get_attributes
import json
import imutils

im_src = cv2.imread('final_hex.jpg')
im_src = imutils.resize(im_src, width=1000)
cv2.imwrite("final_hex.png", im_src)