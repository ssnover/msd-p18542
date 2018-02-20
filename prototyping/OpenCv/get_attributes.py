from pyimagesearch.shapedetector import ShapeDetector
import imutils
import numpy as np
import cv2
from get_coordinate import get_coordinate
from get_rgbcolor import get_rgbcolor


def get_attributes(image):
    hexagon_attributes = []
    pixel_hsv = []
    pixel_hsv_averages = []

    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                         cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()

    #    loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        if M["m10"] == 0:
            M["m10"] = M["m10"]+1
        if M["m00"] == 0:
            M["m00"] = M["m00"]+1

        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        if shape == "hexagon":
            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            px = image[cY, cX]
            print(px)
            pixel_hsv = []
            for i in range(0, 3):
                for k in range(0, 3):
                    pixel = image[cY + i, cX + k]
                    pixel_hsv.insert(i + k, pixel)
                    print(pixel)

            # calculate the average H, S, and V values for each hexagon tile
            average_hsv = np.mean(pixel_hsv, axis=0)
            pixel_hsv_averages.append(np.mean(pixel_hsv, axis=0))
            print(np.mean(pixel_hsv, axis=0))
            print(pixel_hsv_averages)

            hexagon_attributes += [get_rgbcolor(average_hsv)]

            hexagon_attributes += [get_coordinate(px)]

            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 255), 2)


         # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    print(hexagon_attributes)
    return hexagon_attributes
