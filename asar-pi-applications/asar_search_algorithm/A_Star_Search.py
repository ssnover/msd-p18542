from queue import Queue
from queue import PriorityQueue

import json

import math

ter_height = 8  # number of tiles down side
ter_width = 8   # number of tiles across top

mode = 2 #0 for safe, 1 for med, 2 for fast

# Order queue to .get the lowest priority
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

def inst_graph():
    tile = {}

    for x in range(1, ter_height+1):
        for y in range(1, ter_width+1):
            attribute = {}  # prevents the list from overwriting old dictionary keys
            if x % 2 == 0: #x is even
                temp_child = [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x, y+1), (x-1, y)]
            else:
                temp_child = [(x, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y)]
            children = filter(lambda i: 1 <= i[0] <= ter_height and 1 <= i[1] <= ter_width, temp_child)
            attribute['children'] = list(children)
            attribute['im_dngr'] = 0
            attribute['ad_dngr'] = 0
            attribute['speed'] = 0
            tile[(x, y)] = attribute

    # print(tile[(8, 1)])
    # print(tile[(8, 2)])
    # print(tile[(8, 3)])
    # print(tile[(7, 4)])
    # print(tile[(6, 4)])
    # print(tile[(6, 5)])
    return tile

def give_dng(tile):
    terrain = {}
    start = ()
    goal = ()
    for k in range(1, ter_height+1):
        for j in range(1, ter_width+1):
            terrain = json.load(open('terrain.txt'))
            i = terrain['coordinate'].index([k, j])
            if terrain['color'][i] == 'black':
                tile[(k, j)]['im_dngr'] = 200
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'blue':
                tile[(k, j)]['im_dngr'] = 200
                tile[(k, j)]['ad_dngr'] = 0
                tile[(k, j)]['speed'] = 200
            elif terrain['color'][i] == 'red':
                tile[(k, j)]['im_dngr'] = 10
                tile[(k, j)]['ad_dngr'] = 5
                tile[(k, j)]['speed'] = 1
            elif terrain['color'][i] == 'orange':
                tile[(k, j)]['im_dngr'] = 5
                tile[(k, j)]['ad_dngr'] = 2
                tile[(k, j)]['speed'] = 0
            elif terrain['color'][i] == 'green':
                tile[(k, j)]['im_dngr'] = 3
                tile[(k, j)]['ad_dngr'] = 1
                tile[(k, j)]['speed'] = 1
            elif terrain['color'][i] == 'yellow':
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

    #print(tile[(1, 1)])
    # print(tile[(5, 5)])
    # print(tile[(8, 8)])
    # print(goal)
    # print(tile[goal])
    # print(tile)

    return start, goal, tile


def a_star_search(tile, start, goal, mode):
    frontier = MyPriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        i = 0
        current = frontier.get()

        if current == goal:
            break

        for i in range(0, len(tile[current]['children'])):
            next = tile[current]['children'][i]
            new_cost = cost_so_far[current] + travel(current, next, tile)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                if mode == 1:
                    priority = new_cost + med_heuy(goal, next, tile)
                elif mode == 2:
                    priority = new_cost + fast_heuy(goal, next, tile)
                else:
                    priority = new_cost + safe_heuy(goal, next, tile)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, start, goal#, cost_so_far

def travel(current, next, tile):
    travel_cost = tile[next]['speed']
    #travel_cost = math.sqrt(pow((current[0] - next[0]), 2) + pow((current[1] - next[1]), 2))
    return travel_cost

def safe_heuy(goal, next, tile):
    heuy_cost = (tile[next]['im_dngr'] * tile[next]['ad_dngr'])*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    # print(heuy_cost)
    return heuy_cost

def med_heuy(goal, next, tile):
    heuy_cost = tile[next]['im_dngr'] *(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    #print(heuy_cost)
    return heuy_cost

def fast_heuy(goal, next, tile):
    heuy_cost = tile[next]['speed']*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    # print(heuy_cost)
    return heuy_cost

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    print(path)
    return path

def main():
    go_start, go_goal, new_tile = give_dng(inst_graph())
    f_came_from, f_start, f_goal = a_star_search(new_tile, go_start, go_goal, mode)
    reconstruct_path(f_came_from, f_start, f_goal)



if __name__=='__main__':
    main()

