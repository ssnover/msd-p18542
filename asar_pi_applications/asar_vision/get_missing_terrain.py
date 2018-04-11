def get_missing_terrain(hexagon_attributes, coordinate_check):

    differences = []
    color_differences = []

    differences = [i for i in color_differences + hexagon_attributes['coordinate']
                   if i not in color_differences or i not in hexagon_attributes['coordinate']]

    hexagon_attributes['coordinate'] += differences

    for i in range(0, len(differences)):
        color_differences += 'blue'
    hexagon_attributes['color'] += color_differences

    return hexagon_attributes
