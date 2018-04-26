import cv2
import json

path = []
pixel_path = []
# def draw_robot_path(image, path):
image = cv2.imread('hex_t.png')
parameters = json.load(open('terrain.txt'))
path = [[8, 5], [7, 4], [6, 5], [6, 6], [5, 6], [4, 7], [3, 7], [2, 8], [1, 8]]

for j in range(0, len(path)):
    for i in range(0, len(parameters['coordinate'])):
        if path[j][0] == parameters['coordinate'][i][0] and path[j][1] == parameters['coordinate'][i][1]:
            pixel_path.append(parameters['pixel'][i])
thickness = int(5)
tuple(pixel_path)
print(pixel_path)
for k in range(0, len(path)-1):
    cv2.line(image, pixel_path[k], pixel_path[k+1], (0, 0, 255), thickness)

cv2.imshow('path', image)
cv2.waitKey(0)
    # return image
