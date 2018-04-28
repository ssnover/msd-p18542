import cv2
import json

path = []
pixel_path = []
def draw_robot_path(image):
    parameters = json.load(open('terrain.txt'))
    path = []
    path = parameters['path']
    print(len(parameters['pixel']))
    print(len(parameters['coordinate']))
    for i in range(0, len(parameters['pixel'])):
        temp_coordinate = parameters['pixel'][i][0]
        parameters['pixel'][i][0] = parameters['pixel'][i][1]
        parameters['pixel'][i][1] = temp_coordinate

    for j in range(0, len(path)):
        for i in range(0, len(parameters['pixel'])):
            if path[j][0] == parameters['coordinate'][i][0] and path[j][1] == parameters['coordinate'][i][1]:
                pixel_path.append(tuple(parameters['pixel'][i]))
    thickness = int(5)
    tuple(pixel_path)

    for k in range(0, len(pixel_path)-1):
        cv2.line(image, pixel_path[k], pixel_path[k+1], (0, 0, 255), thickness)
        cv2.circle(image, pixel_path[k], 7, (0, 0, 255), -1)

    cv2.imshow('path', image)
    cv2.waitKey(0)
    return image
