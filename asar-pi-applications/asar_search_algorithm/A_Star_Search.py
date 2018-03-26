from queue import Queue
from queue import PriorityQueue

import json

import math

ter_height = 8  # number of tiles down the side
ter_width = 8   # number of tiles across the top

mode = 2  # 0 for safe, 1 for med, 2 for fast


# Modifies queue to .get the lowest priority
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


# inst_graph instantiates the dictionary of tiles with its coordinates and attributes
def inst_graph():
    tile = {}

    for x in range(1, ter_height+1):
        for y in range(1, ter_width+1):
            attribute = {}  # prevents the list from overwriting old dictionary keys
            if x % 2 == 0:  # x is even
                temp_child = [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x, y+1), (x-1, y)]
            else:
                temp_child = [(x, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y)]

            # remove neighbor nodes that are out of grid
            children = filter(lambda i: 1 <= i[0] <= ter_height and 1 <= i[1] <= ter_width, temp_child)
            attribute['children'] = list(children)
            attribute['im_dngr'] = 0
            attribute['ad_dngr'] = 0
            attribute['speed'] = 0
            tile[(x, y)] = attribute

    return tile


# give_dng reads the colors of the tiles from the VisionSys. Modifies attribute values accordingly
def give_dng(tile):
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
                tile[(k, j)]['ad_dngr'] = 2
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


# Main A* algorithm adapted for use with the dictionary of tiles
def a_star_search(tile, start, goal, mode):
    frontier = MyPriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        i = 0
        current = frontier.get()  # pulls the least expensive node off of queue

        if current == goal:  # goal test
            break

        for i in range(0, len(tile[current]['children'])):
            next = tile[current]['children'][i]  # iterates through children of current node
            new_cost = cost_so_far[current] + travel(current, next, tile, mode)  # heuristic part 1 (uses danger & Speed)
            if next not in cost_so_far or new_cost < cost_so_far[next]:  # if next has not been visited
                if tile[next]['speed'] < 200:  # do not evaluate obstacles (Rock & water)
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next, tile)  # heuristic part 2 (Euclidean distance)
                    frontier.put(next, priority)  # put evaluated node onto queue
                    came_from[next] = current

    return came_from, start, goal


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

    return travel_cost


# Part 2 of Heuristics. Euclidean distance is used in absence of a way to estimate the danger/speed of tiles to goal
def heuristic(goal, next, tile):

    heuy_cost = math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2))  # Euclidean Distance

    # if mode == 1:  # med heuristic (account for speed and immediate danger)
    #     # heuy_cost = tile[next]['im_dngr'] *(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    #     # print(heuy_cost)
    # elif mode == 2:  # fast heuristic (ignore danger if the path is quick
    #     # heuy_cost = tile[next]['speed']*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    #     # print(heuy_cost)
    # else:  # default safe heuristic (ignore speed of path, choose based only on dangers)
    #     # heuy_cost = (tile[next]['im_dngr'] * tile[next]['ad_dngr'])*(math.sqrt(pow((goal[0] - next[0]), 2) + pow((goal[1] - next[1]), 2)))
    #     # print(heuy_cost)

    return heuy_cost


# Reconstruct_path pulls the path from the queue
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


# path_to_move converts the path from coordinates to the robot's instruction protocol
def path_to_move(path, tile):
    print(path)

    movement = []

    ori = -120  # import exact orientation from vision system

    for i in range(1, len(path)):
        if tile[path[i]]['speed'] == 0:
            speed = 'ff'
        else:
            speed = '55'

        if path[i-1][0] % 2 == 0:  #is even
            if path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:
                turn = 60 - ori
                ori = 60
            elif path[i][0] < path[i-1][0] and path[i][1] < path[i-1][1]:
                turn = 120 - ori
                ori = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:
                turn = 180 - ori
                ori = 180
            elif path[i][0] > path[i-1][0] and path[i][1] < path[i-1][1]:
                turn = ori + 120
                ori = -120
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:
                turn = ori + 60
                ori = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:
                turn = 0 - ori
                ori = 0
            else:
                turn = 0
                speed = 0
        else:
            if path[i][0] < path[i-1][0] and path[i][1] > path[i-1][1]:
                turn = 60 - ori
                ori = 60
            elif path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:
                turn = 120 - ori
                ori = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:
                turn = 180 - ori
                ori = 180
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:
                turn = ori + 120
                ori = -120
            elif path[i][0] > path[i-1][0] and path[i][1] > path[i-1][1]:
                turn = ori + 60
                ori = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:
                turn = 0 - ori
                ori = 0
            else:
                turn = 0
                speed = 0

        # convert the 'out of hex range' angles to their equivalents in range
        if turn == 340:
            turn = -120
        elif turn == 240:
            turn = -60

        # identify positive/negative rotation
        if turn > 0:
            rot = 'aa'  # rotate left
        else:
            rot = 'bb'  # rotate right

        # add a turn + drive instruction
        movement.append('ff{0}{1}f0ffcc28{2}f0'.format(rot, hex(abs(turn))[2:].zfill(2), speed))

    movement.append('ffffff')  # end transmission

    trail = ''.join(movement)  # convert transmission list to string

    for i in range(0, len(movement)):  # optional vertical display of instructions
        print(movement[i])

    print(trail)

    return trail



def main():
    go_start, go_goal, new_tile = give_dng(inst_graph())
    f_came_from, f_start, f_goal = a_star_search(new_tile, go_start, go_goal, mode)
    path_to_move(reconstruct_path(f_came_from, f_start, f_goal), new_tile)



if __name__=='__main__':
    main()

