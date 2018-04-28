
import numpy as np
import cv2
from utils import get_four_points
import json

upper_bound = []
lower_bound = []
rgb_color = []
parameters = {}
parameters['color'] = []
parameters['value'] = []
parameters['corners'] = []
pixel_hsv_averages = []
gray = "gray"
blue = "blue"
green = "green"
red = "red"
yellow = "yellow"
pink = "pink"
orange = "orange"
purple = "purple"
# black = "black"
im_src = cv2.imread('terrain_example_fieldhouse.jpg')

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

print('Click on the four corners of the book -- top left first and bottom left last -- and then hit ENTER')


# Show image and wait for 4 clicks.
cv2.imshow("Image", im_src)
pts_src = get_four_points(im_src);
parameters['corners'] = pts_src.tolist()
# Calculate the homography
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination
im_dst = cv2.warpPerspective(im_src, h, size[0:2])


# Show output
cv2.imshow("Image", im_dst)
cv2.waitKey(0)
print('First start by clicking on all red tiles')
print('proceed to click on a blue tile\n then green...\n gray\n orange\n purple')
parameters['color'] = [red, blue, green, gray, orange, purple]
hsv = cv2.cvtColor(im_dst, cv2.COLOR_BGR2HSV)
points = get_four_points(im_dst)
pixel_hsv = []
for k in range(0, len(points)):
    y = np.int64(points[k][1])
    x = np.int64(points[k][0])
    for i in range(0, 5):
        for j in range(0, 5):
            pixel = im_dst[y + i, x + j]
            color = np.uint8([[[pixel[0], pixel[1], pixel[2]]]])
            pixel = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
            pixel_hsv.insert(i + j, pixel)
    pixel_hsv_averages.append(np.mean(pixel_hsv, axis=0).tolist())
    print(np.mean(pixel_hsv, axis=0))

parameters['value'].append(pixel_hsv_averages)

with open('parameters.txt', 'w') as outfile:
    json_str = json.dump(parameters, outfile)

    print(json_str)
'''   
blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]

for i in range(0, len(points)):

    color_point_x = np.int64(points[i][0])
    color_point_y = np.int64(points[i][1])

    rgb_color.append(im[color_point_y, color_point_x])

for i in range(0, len(rgb_color)):
    blue = rgb_color[i][0]
    green = rgb_color[i][1]
    red = rgb_color[i][2]
    color = np.uint8([[[blue, green, red]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]

    lower_bound += [hue - 10, 100, 100]
    upper_bound += [hue + 10, 255, 255]
    parameters['value'].append(hsv_color.tolist()[0][0])
'''