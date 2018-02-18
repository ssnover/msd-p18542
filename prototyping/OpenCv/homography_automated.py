import cv2
import numpy as np
from utils import get_four_points
from pyimagesearch.shapedetector import ShapeDetector
import imutils
from four_corners import four_points

if __name__ == '__main__':
    # Read in the image.
    im_src = cv2.imread('hex_t.png')
    '''
    imgray = cv2.cvtColor(im_src,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(im_src, contours, -1, (0, 255, 0), 3)
    cv2.imshow('im_src', im_src)
    k = cv2.waitKey(0)
    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()

    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        shape = sd.detect(c)

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c = c.astype("int")
        # set px equal to the coordinate value of the centroid of each hexagon
        px = image[cY, cX]
        print(px)
        print(cX, cY)
        '''
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
    '''
    # Draw the contours around each shape, the circle in the center and name the shape
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

        Click on the four corners of the book -- top left first and
        bottom left last -- and then hit ENTER
        '''

    # Show image and wait for 4 clicks.
    cv2.imshow("Image", im_src)
    pts_src = four_points(im_src)
    print(pts_src)
    print(pts_dst)
    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])
    # print(pts_src)
    print(pts_dst)
    # Show output
    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)

