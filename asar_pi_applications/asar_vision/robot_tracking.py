import imutils
import cv2
import numpy as np
import math
from math import sqrt

def find_robot_orientation(image):
    robot = {}
    robot['angle'] = []
    robot['direction'] = []
    robotLower = (161, 174, 236)
    robotUpper = (255, 255, 255)
    distances = []
    # img = cv2.imread('all_color_terrain_with_robot.png')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, robotLower, robotUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    # find contours in thresholded image, then grab the largest
    # one
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key=cv2.contourArea)
    M = cv2.moments(c)

    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    # determine the most extreme points along the contour
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    print(extBot, extLeft, extRight, extTop, (cx, cy))
    # Take care of the extra point, because there are only 3 sides,
    # the distance max will be flawed of far point is 2 points (ie bottom and right)
    if abs(extLeft[0] - extRight[0]) < 10 and abs(extLeft[1] - extRight[1]) < 10:
        extRight = (cx, cy)
    if abs(extLeft[0] - extTop[0]) < 10 and abs(extLeft[1] - extTop[1]) < 10:
        extTop = (cx, cy)
    if abs(extLeft[0] - extBot[0]) < 10 and abs(extLeft[1] - extBot[1]) < 10:
        extBot = (cx, cy)
    if abs(extBot[0] - extRight[0]) < 10 and abs(extBot[1] - extRight[1]) < 10:
        extRight = (cx, cy)
    if abs(extTop[0] - extRight[0]) < 10 and abs(extTop[1] - extRight[1]) < 10:
        extRight = (cx, cy)

    # draw the outline of the object, then draw each of the
    # extreme points, where the left-most is red, right-most
    # is green, top-most is blue, and bottom-most is teal
    cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
    cv2.circle(image, (cx, cy), 7, (255, 0, 255), -1)
    cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
    cv2.circle(image, extRight, 6, (0, 255, 0), -1)
    cv2.circle(image, extTop, 6, (255, 0, 0), -1)
    cv2.circle(image, extBot, 6, (255, 255, 0), -1)

    # create list of extreme points
    extreme_points = (extLeft, extRight, extTop, extBot)
    for i in range(0, len(extreme_points)):
        dist = sqrt((extreme_points[i][0] - extLeft[0]) ** 2 +
                    (extreme_points[i][1] - extLeft[1]) ** 2 +
                    (extreme_points[i][0] - extRight[0]) ** 2 +
                    (extreme_points[i][1] - extRight[1]) ** 2 +
                    (extreme_points[i][0] - extBot[0]) ** 2 +
                    (extreme_points[i][1] - extBot[1]) ** 2 +
                    (extreme_points[i][0] - extTop[0]) ** 2 +
                    (extreme_points[i][1] - extTop[1]) ** 2)

        distances += [dist]
    index_min = np.argmax(distances)
    print(distances)
    top_triangle = (extreme_points[index_min])
    print(top_triangle)
    center = (cx, cy)
    # Create vector containing the top of the isosceles triangle
    # and the center of the contour that was found
    centerline_points = [center, top_triangle]
    # draw a line through the triangle in the direction of the robot motion
    rows, cols = image.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(np.float32(centerline_points), cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv2.line(image, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
    # find the angle of the robot
    rad = math.atan2(vx, vy)
    angle = math.degrees(rad)
    '''
    # fix the angle such that the tip pointing up is 0deg,
    # movement to the right of that is +deg
    # movement to the left is -deg
    # angle measurements are from -180:180
    '''
    if top_triangle[0] < center[0]:
        angle = -angle
    if top_triangle[0] > center[0]:
        angle = 180 - angle
    angle = round(angle)
    print(angle)

    cv2.putText(image, str(angle), (int(cx) - 50, int(cy) - 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2,
                cv2.LINE_AA)
    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    return angle, center



'''
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
'''
