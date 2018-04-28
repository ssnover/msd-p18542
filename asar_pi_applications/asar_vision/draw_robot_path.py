import cv2
#import json

path = []
pixel_path = []
def draw_robot_path(image, coordinates):
    #parameters = json.load(open('terrain.txt'))

    for i in range(0, len(coordinates)):
        temp_coordinate = coordinates[i][0]
        coordinates[i][0] = coordinates[i][1]
        coordinates[i][1] = temp_coordinate

    for j in range(0, len(path)):
        for i in range(0, len(coordinates)):
            if path[j][0] == coordinates[i][0] and path[j][1] == coordinates[i][1]:
                pixel_path.append(tuple(coordinates[i]))
    thickness = int(5)
    tuple(pixel_path)

    for k in range(0, len(pixel_path)-1):
        cv2.line(image, pixel_path[k], pixel_path[k+1], (0, 0, 255), thickness)
        cv2.circle(image, pixel_path[k], 7, (0, 0, 255), -1)

    return image
