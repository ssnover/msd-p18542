import json
import logging

logging.basicConfig(filename='search.log', level=logging.INFO)

TERRAIN_HEIGHT = 8  # number of tiles down the side
TERRAIN_WIDTH = 8   # number of tiles across the top

INFINITY = 200  # variable representing impassable terrain

SAFE_LIMIT = 25  # danger max for safe mode travel

# hex speeds for terrain types
FAST = 'FF'
MEDIUM = 'C8'
SLOW = '7D'


# give_dng reads the colors of the tiles from the VisionSys. Modifies attribute values accordingly
# color counter added to handle errors
def give_danger(tile, terrain_path):
    start = ()
    goal = ()
    pink = 0
    purple = 0
    for k in range(1, TERRAIN_HEIGHT+1):
        for j in range(1, TERRAIN_WIDTH+1):
            terrain = json.load(open(terrain_path))
            i = terrain['coordinate'].index([k, j])
            if terrain['color'][i] == 'blu':
                tile[(k, j)]['immediate_danger'] = 200
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'red':
                tile[(k, j)]['immediate_danger'] = 25
                tile[(k, j)]['adjacent_danger'] = 3
                tile[(k, j)]['speed'] = 3
            elif terrain['color'][i] == 'org':
                tile[(k, j)]['immediate_danger'] = 3
                tile[(k, j)]['adjacent_danger'] = 1
                tile[(k, j)]['speed'] = 1
            elif terrain['color'][i] == 'grn':
                tile[(k, j)]['immediate_danger'] = 2
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 2
            elif terrain['color'][i] == 'gry':
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'ukn':  # flagged unknown tiles
                tile[(k, j)]['immediate_danger'] = 200
                tile[(k, j)]['adjacent_danger'] = 3
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'pnk':  # robot
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
                start = (k, j)
                pink = pink + 1
            elif terrain['color'][i] == 'prp':  # victim
                tile[(k, j)]['immediate_danger'] = 0
                tile[(k, j)]['adjacent_danger'] = 0
                tile[(k, j)]['speed'] = 0
                goal = (k, j)
                purple = purple + 1
            else:
                tile[(k, j)]['immediate_danger'] = 200
                tile[(k, j)]['adjacent_danger'] = 3
                tile[(k, j)]['speed'] = 200

    if purple == 0:
        raise ValueError('No victim identified')
    elif purple > 1:
        raise ValueError('Too many victims')
    elif pink == 0:
        raise ValueError('No ASAR unit identified')
    elif pink > 1:
        raise ValueError('Too many ASAR units')

    orientation = -1*terrain['robot orientation'] + 90

    if orientation == 270:
        orientation = -90
    elif orientation == -270:
        orientation = 90

    return start, goal, tile, orientation


# travel is part 1 of the heuristic. assigns priority of tiles adjacent to current tile
def travel(current, next, tile, mode):
    if mode == 1:  # smart heuristic (account for speed and immediate danger)

        adjacent_danger = []
        for item in tile[next]['children']:
            adjacent_danger.append(tile[item]['adjacent_danger'])

        travel_cost = 1 + tile[next]['immediate_danger'] + tile[next]['speed'] + sum(adjacent_danger)/10

    elif mode == 2:  # fast heuristic (ignore danger if the path is quick

        travel_cost = 1 + tile[next]['speed']

    elif mode == 3:  # direct heuristic (ignores danger and speed, uses only distance)

        travel_cost = 1

    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        adjacent_danger = []
        for item in tile[next]['children']:
            adjacent_danger.append(tile[item]['adjacent_danger'])
            # print(tile[item]['adjacent_danger'])

        travel_cost = 1 + tile[next]['immediate_danger'] + sum(adjacent_danger)

    # print('{0} --> {1} = {2}'.format(current, next, travel_cost))

    return travel_cost


def floor(x):
    if x >= 0:
        x = x >> 1
    else:
        x = (x-1) / 2

    return x


def ceil(x):
    if x >= 0:
        x = (x+1) >> 1
    else:
        x = x/2

    return x


# Part 2 of Heuristics. Euclidean distance is used in absence of a way to estimate the danger/speed of tiles to goal
def heuristic(goal, next, tile, mode):

    ax = next[1] - floor(next[0])
    ay = next[1] + ceil(next[0])
    bx = goal[1] - floor(goal[0])
    by = goal[1] + ceil(goal[0])
    dx = bx - ax
    dy = by - ay

    if (dx * dy) > 0:
        hexagonal_manhattan_distance = max(abs(dx), abs(dy))
    # elif np.sign(dx) != np.sign(dy) and abs(dx) == abs(dy):
    #     hexagonal_manhattan_distance = max(abs(dx), abs(dy))+1
    else:
        hexagonal_manhattan_distance = abs(dx) + abs(dy)

    if mode == 1:  # smart heuristic (account for speed and immediate danger)
        heuristic_cost = hexagonal_manhattan_distance
        # logging.info(heuristic_cost)
    elif mode == 2:  # fast heuristic (ignore danger if the path is quick
        heuristic_cost = hexagonal_manhattan_distance
        # logging.info(heuristic_cost)
    elif mode == 3:  # direct heuristic (distance only)
        heuristic_cost = hexagonal_manhattan_distance
        # logging.info(heuristic_cost)
    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        heuristic_cost = hexagonal_manhattan_distance
        # logging.info(heuristic_cost)

    return heuristic_cost
