import math
import json

TERRAIN_HEIGHT = 8  # number of tiles down the side
TERRAIN_WIDTH = 8   # number of tiles across the top

mode = 2  # 0 for safe, 1 for smart, 2 for fast
INFINITY = 200  # variable representing impassable terrain

SAFE_LIMIT = 25  # danger max for safe mode travel

# hex speeds for modes
FAST = 'FF'
SMART = 'C8'
SAFE = '7D'

# initial robot orientation [read from mark's Json eventually]
orientation = 0


# give_dng reads the colors of the tiles from the VisionSys. Modifies attribute values accordingly
# color counter added to handle errors
def give_danger(tile):
    start = ()
    goal = ()
    white = 0
    purple = 0
    for k in range(1, TERRAIN_HEIGHT+1):
        for j in range(1, TERRAIN_WIDTH+1):
            terrain = json.load(open('terrain.txt'))
            i = terrain['coordinate'].index([k, j])
            if terrain['color'][i] == 'blue':
                tile[(k, j)]['immediate_danger'] = 200
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'red':
                tile[(k, j)]['immediate_danger'] = 25
                tile[(k, j)]['adjacent_danger'] = 3
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'orange':
                tile[(k, j)]['immediate_danger'] = 2
                tile[(k, j)]['adjacent_danger'] = 1
                tile[(k, j)]['speed'] = 1
            elif terrain['color'][i] == 'green':
                tile[(k, j)]['immediate_danger'] = 2
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 2
            elif terrain['color'][i] == 'gray':
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'white':
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
                start = (k, j)
                white = white + 1
            elif terrain['color'][i] == 'purple':
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
                goal = (k, j)
                purple = purple + 1
            else:
                tile[(k, j)]['immediate_danger'] = 200
                tile[(k, j)]['adjacent_danger'] = 2
                tile[(k, j)]['speed'] = 200

    if purple != 1:
        raise ValueError('Goal DNE')
    elif white != 1:
        raise ValueError('Robot cannot be identified')

    return start, goal, tile


# travel is part 1 of the heuristic. assigns priority of tiles adjacent to current tile
def travel(current, next, tile, mode):
    if mode == 1:  # smart heuristic (account for speed and immediate danger)
        travel_cost = tile[next]['immediate_danger'] + tile[next]['speed']
    elif mode == 2:  # fast heuristic (ignore danger if the path is quick
        travel_cost = tile[next]['speed'] * tile[next]['immediate_danger']
    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        adjacent_danger = []
        for item in tile[next]['children']:
            adjacent_danger.append(tile[item]['adjacent_danger'])
            # print(tile[item]['adjacent_danger'])

        travel_cost = tile[next]['immediate_danger'] + sum(adjacent_danger)

    # print('{0} --> {1} = {2}'.format(current, next, travel_cost))

    return travel_cost


# Part 2 of Heuristics. Euclidean distance is used in absence of a way to estimate the danger/speed of tiles to goal
def heuristic(goal, next, tile):

    if mode == 1:  # smart heuristic (account for speed and immediate danger)
        heuristic_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # print(heuristic_cost)
    elif mode == 2:  # fast heuristic (ignore danger if the path is quick
        heuristic_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # print(heuristic_cost)
    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        heuristic_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # print(heuristic_cost)

    return heuristic_cost
