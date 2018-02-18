from utils import get_four_points
from pyimagesearch.shapedetector import ShapeDetector

import numpy as np
import imutils
import cv2
if __name__ == '__main__':
    # initialize the pixel value list
    pixel_hsv = []
    # Read in the image.
    im_src = cv2.imread("hex_t.png")

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
    cv2.imshow("Image", im_src)
    pts_src = get_four_points(im_src);

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)

    image = im_dst
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

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
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        # set px equal to the coordinate value of the centroid of each hexagon
        px = image[cY, cX]
        print(px)
        print(cX, cY)
        # clear the list and gather the HSV values of the 9 pixels around the centroid
        pixel_hsv = []
        for i in range(0, 3):
            for k in range(0, 3):
                pixel = image[cY + i, cX + k]
                pixel_hsv.insert(i + k, pixel)
                print(pixel)
                print(pixel_hsv)
        # calculate the average H, S, and V values for each hexagon tile
        print(np.mean(pixel_hsv, axis=0))

        # Draw the contours around each shape, the circle in the center and name the shape
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)



        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)