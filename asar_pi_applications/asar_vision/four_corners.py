# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import numpy as np
import cv2


def four_points(image):


    four = {}
    four['points'] = []
    four['corners'] = [[0, 0], [0, 0], [0, 0], [0, 0]]
    four_corners = []

    # load the image and resize it to a smaller factor so that
    # the shapes can be approximated better
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
        if shape == "triangle":
            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            px = image[cY, cX]
            # print(px)

            # cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            #cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
               #     0.5, (255, 255, 255), 2)
            # print(cX, cY)

            if len(four_corners) < 4:
                four_corners.append([cX, cY])

                print(four_corners)
                # cv2.imshow("Image", image)
            # cv2.waitKey(0)

    # show the output image
    # four_corners.reverse()
    for i in range(0, len(four_corners)):
        if four_corners[i][0] < 50 and four_corners[i][1] < 50:
            four['corners'][0] = four_corners[i]
        elif four_corners[i][0] > 600 and four_corners[i][1] < 50:
            four['corners'][1] = four_corners[i]
        elif four_corners[i][0] > 600 and four_corners[i][1] > 500:
            four['corners'][2] = four_corners[i]
        elif four_corners[i][0] < 50 and four_corners[i][1] > 500:
            four['corners'][3] = four_corners[i]
    print(four['corners'])
    # four['corners'] = four_corners
    four = np.vstack(four['corners']).astype(float)

    return four


