import cv2
import numpy as np
from four_corners import four_points
from get_attributes import get_attributes
import json
import imutils
import os


def automated_homography(input_image=None):
    if input_image is None:
        im_src = cv2.imread('new_terrain_for_andrew.png')
    else:
        im_src = cv2.imread(input_image)
    final_attributes = []
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

    # Show image and wait for 4 clicks.
    # cv2.imshow("Image", im_src)
    pts_src = four_points(im_src)
    print(pts_src)
    print(pts_dst)
    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])
    # print(pts_src)

    attributes = get_attributes(im_dst)
    print(pts_dst)
    # with attributes as outfile:

    # Show output

    # cv2.imshow("Image", im_dst)

    with open('terrain.txt', 'w') as outfile:
        json_str = json.dump(attributes, outfile)

    print(json_str)


    # cv2.waitKey(0)
    return os.path.abspath('terrain.txt')

if __name__ == '__main__':


    # Read in the image.
    automated_homography()







