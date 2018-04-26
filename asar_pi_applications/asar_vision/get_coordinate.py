def get_coordinate(px):
    x = px[1]
    y = px[0]
    range_min_x = []
    range_min_y = []
    range_max_x = []
    range_max_y = []
    pixel_range = {}
    pixel_range['y'] = []
    pixel_range['x'] = []
    coordinate = [9, 9]

    startx = 69
    starty = 40
    for j in range(1, 9):
        range_min_y = starty - 15
        range_max_y = starty + 15

        for i in range(1, 9):
            range_min_x = startx - 15
            range_max_x = startx + 15
            if j % 2 == 0:
                startx = 29 + 71 * (i - 1)
            else:
                startx = 71 + 71 * (i - 1)

            pixel_range['x'] += [(range_min_x, range_max_x)]
            pixel_range['y'] += [(range_min_y, range_max_y)]
        starty = starty + 61
    for k in range(0, len(pixel_range['x'])):
        if pixel_range['x'][k][1] > x > pixel_range['x'][k][0]:
            if k > 8:
                k = k-8
            if k == 0:
                k = k+1
            coordinate[1] = k
            break
    for m in range(0, len(pixel_range['y'])):
         if pixel_range['y'][m][1] > y > pixel_range['y'][m][0]:
             coordinate[0] = (m // 8)+1
             break
    if coordinate[0] == 9 or coordinate[1] == 9:
        return None

    return coordinate
