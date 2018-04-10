import math

import json

ter_height = 8  # number of tiles down the side
ter_width = 8   # number of tiles across the top

mode = 2  # 0 for safe, 1 for smart, 2 for fast
inf = 200 # variable representing impassable terrain

safeLimit = 25  # danger max for safemode travel

# hex speeds for modes
fast = 'FF'
smart = 'C8'
safe = '7D'

# initial robot orientation [read from mark's Json eventually]
orientation = 0

# give_dng reads the colors of the tiles from the VisionSys. Modifies attribute values accordingly
def give_dng(tile):
    start = ()
    goal = ()
    for k in range(1, ter_height+1):
        for j in range(1, ter_width+1):
            terrain = json.load(open('terrain.txt'))
            i = terrain['coordinate'].index([k, j])
            if terrain['color'][i] == 'blue':
                tile[(k, j)]['im_dngr'] = 200
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'red':
                tile[(k, j)]['im_dngr'] = 25
                tile[(k, j)]['ad_dngr'] = 3
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'orange':
                tile[(k, j)]['im_dngr'] = 2
                tile[(k, j)]['ad_dngr'] = 1
                tile[(k, j)]['speed'] = 1
            elif terrain['color'][i] == 'green':
                tile[(k, j)]['im_dngr'] = 2
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 2
            elif terrain['color'][i] == 'gray':
                tile[(k, j)]['im_dngr'] = 0
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'white':
                tile[(k, j)]['im_dngr'] = 0
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 0
                start = (k, j)
            elif terrain['color'][i] == 'purple':
                tile[(k, j)]['im_dngr'] = 0
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 0
                goal = (k, j)
            else:
                tile[(k, j)]['im_dngr'] = 200
                tile[(k, j)]['ad_dngr'] = 2
                tile[(k, j)]['speed'] = 200

    return start, goal, tile

# travel is part 1 of the heuristic. assigns priority of tiles adjacent to current tile
def travel(current, next, tile, mode):
    if mode == 1:  # med heuristic (account for speed and immediate danger)
        travel_cost = tile[next]['im_dngr'] + tile[next]['speed']
    elif mode == 2:  # fast heuristic (ignore danger if the path is quick
        travel_cost = tile[next]['speed'] * tile[next]['im_dngr']
    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        ad_dngr = []
        for item in tile[next]['children']:
            ad_dngr.append(tile[item]['ad_dngr'])
            #print(tile[item]['ad_dngr'])

        travel_cost = tile[next]['im_dngr'] + sum(ad_dngr)

    # print('{0} --> {1} = {2}'.format(current, next, travel_cost))

    return travel_cost

# Part 2 of Heuristics. Euclidean distance is used in absence of a way to estimate the danger/speed of tiles to goal
def heuristic(goal, next, tile):


    if mode == 1:  # med heuristic (account for speed and immediate danger)
        heuy_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # heuy_cost = tile[next]['im_dngr'] *(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
        # print(heuy_cost)
    elif mode == 2:  # fast heuristic (ignore danger if the path is quick
        heuy_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # heuy_cost = tile[next]['speed']*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
        # print(heuy_cost)
    else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
        heuy_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance
        # heuy_cost = (tile[next]['im_dngr'] * tile[next]['ad_dngr'])*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
        # print(heuy_cost)

    return heuy_cost
