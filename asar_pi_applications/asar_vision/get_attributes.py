from .pyimagesearch.shapedetector import ShapeDetector
import imutils
import numpy as np
import cv2
from .get_coordinate import get_coordinate
from .get_rgbcolor import get_rgbcolor
from .coordinate_checklist import coordinate_checklist
from .get_missing_terrain import get_missing_terrain
from .robot_tracking import find_robot_orientation
from .robot_distance_incorrect import robot_distance_incorrect
from .find_victim import find_victim


def get_attributes(image):

    number_of_hexagons = 0
    hexagon_attributes = {}
    robot_tracking = {}
    hexagon_pixel_values = []
    robot_actual_location = []
    hexagon_attributes['color'] = []
    hexagon_attributes['coordinate'] = []
    hexagon_attributes['pixel'] = []
    hexagon_attributes['robot distance incorrect'] = []
    hexagon_attributes['robot orientation'] = []
    hexagon_attributes['robot location'] = []
    hexagon_attributes['robot coordinate'] = []
    hexagon_attributes['victim coordinate'] = []
    final_list_coordinate = []
    final_list_color = []
    final_list_pixel = []
    pixel_hsv = []
    pixel_hsv_averages = []
    coordinate_check = []
    thresh_points = []
    canny_points = []
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    canny_points = [0, 10, 20, 25, 30, 35, 40, 45, 50]
    thresh_points = [80, 90, 100, 110, 120, 130, 140]
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(gray, (2, 2), 0)
    for k in range(0, len(thresh_points)):
        thresh = cv2.threshold(blurred, thresh_points[k], 255, cv2.THRESH_BINARY)[1]
        # canny_edge = cv2.Canny(blurred, canny_points[k], 40)
        # cv2.imshow('thresh', thresh)
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

            cX = int((M["m10"] / M["m00"])) #   * ratio)
            cY = int((M["m01"] / M["m00"]))#   * ratio)
            shape = sd.detect(c)
            if shape == "hexagon" and 150 > len(c) > 100:
                # multiply the contour (x, y)-coordinates by the resize ratio,
                # then draw the contours and the name of the shape on the image
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                c = c.astype("float")
                # c *= ratio
                c = c.astype("int")
                px = [cY, cX]
                # print(px)
                pixel_hsv = []
                for i in range(0, 1):
                    for k in range(0, 1):
                        pixel = image[cY + i, cX + k]
                        pixel_hsv.insert(i + k, pixel)
                        # print(pixel)

                # calculate the average H, S, and V values for each hexagon tile
                average_rgb = np.mean(pixel_hsv, axis=0)
                pixel_hsv_averages.append(np.mean(pixel_hsv, axis=0))
                # return all of the hexagon attributes from called functions
                temp_coordinate = get_coordinate(px)
                if temp_coordinate is not None:
                    average_hsv = np.uint8([[[average_rgb[0], average_rgb[1], average_rgb[2]]]])
                    average_hsv = cv2.cvtColor(average_hsv, cv2.COLOR_BGR2HSV)
                    hexagon_attributes['color'].append(get_rgbcolor(average_hsv))
                    hexagon_pixel_values.append(px)
                    hexagon_attributes['coordinate'].append(get_coordinate(px))
                    number_of_hexagons = number_of_hexagons + 1
                    # remove the duplicates found in the terrain
                    if hexagon_attributes['coordinate'][number_of_hexagons - 1] not in final_list_coordinate:
                        final_list_coordinate.append(hexagon_attributes['coordinate'][number_of_hexagons - 1])
                        final_list_color.append(hexagon_attributes['color'][number_of_hexagons - 1])
                        final_list_pixel.append(hexagon_pixel_values[number_of_hexagons-1])
                        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                # cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
                # cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                 #           0.5, (255, 255, 255), 2)
            # show the output image
            # cv2.imshow("Image", image)
            # cv2.waitKey(0)

    # reset the hexagon attribute lists to the final lists without duplicates
    hexagon_attributes['coordinate'] = final_list_coordinate
    hexagon_attributes['color'] = final_list_color
    hexagon_attributes['pixel'] = final_list_pixel
    # find the robot orientation and direction of travel

    robot_attributes = find_robot_orientation(image)
    robot_actual_location = robot_attributes[1]
    angle = robot_attributes[0]
    hexagon_attributes['robot orientation'] = angle
    robot_distance_movement = robot_distance_incorrect(robot_actual_location, hexagon_pixel_values)
    hexagon_attributes['robot distance incorrect'] = robot_distance_movement
    hexagon_attributes['robot location'] = robot_actual_location
    '''
    for i in range(0, len(hexagon_attributes['coordinate'])):
        if hexagon_attributes['robot coordinate'][0] == hexagon_attributes['coordinate'][i][0] \
                and hexagon_attributes['robot coordinate'][1] == hexagon_attributes['coordinate'][i][1]:
            hexagon_attributes['color'].append("pnk")
    '''
    coordinate_check = coordinate_checklist()
    hexagon_attributes = get_missing_terrain(hexagon_attributes, coordinate_check)
    return hexagon_attributes
