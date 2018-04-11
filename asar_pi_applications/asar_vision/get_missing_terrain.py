def get_missing_terrain(hexagon_attributes, coordinate_check):

    differences = []
    color_differences = []
    blue = "blue"
    differences = [i for i in coordinate_check + hexagon_attributes['coordinate']
                   if i not in coordinate_check or i not in hexagon_attributes['coordinate']]

    hexagon_attributes['coordinate'] += differences

    for i in range(0, len(differences)):
        color_differences.append(blue)
    hexagon_attributes['color'] += color_differences

    return hexagon_attributes
