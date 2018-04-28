import cv2
import numpy as np
from four_corners import four_points
from get_attributes import get_attributes
from draw_robot_path import draw_robot_path
import json
import os


def automated_homography(input_image=None):
    if input_image is None:
        im_src = cv2.imread('terrain_example_fieldhouse.jpg')
    else:
        im_src = cv2.imread(input_image)

    # im_src = cv2.cvtColor(im_src, cv2.COLOR_BGR2HSV)
    # Destination image
    size = (600, 500, 3)

    im_dst = np.zeros(size, np.uint8)

    pts_dst = np.array(
        [
            [0, 0],
            [size[0] - 1, 0],
            [size[0] - 1, size[1] - 1],
            [0, size[1] - 1]
        ], dtype=float
    )
    pts_src = four_points(im_src)
    # Calculate the homography to transform the image
    h, status = cv2.findHomography(pts_src, pts_dst)
    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])
    # cv2.imshow('image', im_dst)
    # cv2.waitKey(0)
    attributes = get_attributes(im_dst)

    with open('terrain.txt', 'w') as outfile:
        json_str = json.dump(attributes, outfile)
    # Show output

    im_dst = draw_robot_path(im_dst)
    # cv2.imshow("Image", im_dst)
    # cv2.waitKey(0)

    return os.path.abspath('terrain.txt')


if __name__ == '__main__':

    automated_homography()







