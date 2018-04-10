from queue import PriorityQueue
import Pi_Cfg as cfg
import base64

ter_height = cfg.ter_height  # number of tiles down the side
ter_width = cfg.ter_width   # number of tiles across the top

mode = cfg.mode  # 0 for safe, 1 for med, 2 for fast


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
            print('Goal Reached!')
            break


        for i in range(0, len(tile[current]['children'])):
            next = tile[current]['children'][i]  # iterates through children of current node
            new_cost = cost_so_far[current] + cfg.travel(current, next, tile, mode)  # heuristic part 1 (uses danger & Speed)
            if next not in cost_so_far or new_cost < cost_so_far[next]:  # if next has not been visited
                if tile[next]['speed'] < 200:  # do not evaluate obstacles (Rock & water)
                    if mode == 0 and tile[next]['im_dngr'] >= cfg.safeLimit:  # do not drive through fire in safe mode
                        continue
                    else:
                        cost_so_far[next] = new_cost
                        priority = new_cost + cfg.heuristic(goal, next, tile)  # heuristic part 2 (Euclidean distance)
                        #print('{0} --> {1} = {2}'.format(current, next, priority))
                        frontier.put(next, priority)  # put evaluated node onto queue
                        came_from[next] = current



    return came_from, start, goal



# Reconstruct_path pulls the path from the queue
def reconstruct_path(came_from, start, goal):
    current = goal
    if current in came_from:
        print('')
    else:
        print('Victim Lost')
        return -1
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


# path_to_move converts the path from coordinates to the robot's instruction protocol
def path_to_move(path, tile):

    if path == -1:
        return 'Search Failed'

    print(path)

    movement = []  # list of robot instructions

    ori = cfg.orientation  # import exact orientation from vision system (current orientation variable)

    for i in range(1, len(path)):

        # convert heuristic speed to hex speed
        if tile[path[i]]['speed'] == 0:  # fast
            speed = cfg.fast
        elif tile[path[i]]['speed'] == 1:  # smart
            speed = cfg.smart
        else:  # default speed for unknown objects == slow
            speed = cfg.safe

        # choose appropriate relative angle to turn based on current orientation and relative position of next tile
        if path[i-1][0] % 2 == 0:  # tile's row is even
            if path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:  # move up && right
                turn = 60 - ori
                ori = 60
            elif path[i][0] < path[i-1][0] and path[i][1] < path[i-1][1]:  # move up && left
                turn = 120 - ori
                ori = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:  # move left
                turn = 180 - ori
                ori = 180
            elif path[i][0] > path[i-1][0] and path[i][1] < path[i-1][1]:  # move down && left
                turn = ori + 120
                ori = -120
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:  # move down && right
                turn = ori + 60
                ori = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:  # move right
                turn = 0 - ori
                ori = 0
            else:  # default no move
                turn = 0
                speed = 0
        else:  # tile's row is odd
            if path[i][0] < path[i-1][0] and path[i][1] > path[i-1][1]:  # move up && right
                turn = 60 - ori
                ori = 60
            elif path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:  # move up && left
                turn = 120 - ori
                ori = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:  # move left
                turn = 180 - ori
                ori = 180
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:  # move down && left
                turn = ori + 120
                ori = -120
            elif path[i][0] > path[i-1][0] and path[i][1] > path[i-1][1]:  # move down && right
                turn = ori + 60
                ori = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:  # move right
                turn = 0 - ori
                ori = 0
            else:  # default no move
                turn = 0
                speed = 0

        # convert the 'out of hex range' angles to their equivalents in range
        if turn == 340:
            turn = -120
        elif turn == 240:
            turn = -60

        # identify positive/negative rotation
        if turn > 0:
            rot = 'AA'  # rotate left
        else:
            rot = 'BB'  # rotate right

        # add a turn + drive instruction to list of movements
        if turn == 0:
            movement.append('FFCC28{0}F0'.format(speed))
        else:
            movement.append('FF{0}{1}F0'.format(rot, format(abs(turn), '02X')))
            movement.append('FFCC28{0}F0'.format(speed))

    movement.append('FFFFFF')  # end transmission

    trail = ''.join(movement)  # convert transmission list to string

    # for i in range(0, len(movement)):  # optional vertical display of instructions
    #     print(movement[i])

    print(trail)

    binary_trail = base64.b16decode(trail)


    #print(binary_trail)

    return trail



def main():
    go_start, go_goal, new_tile = cfg.give_dng(inst_graph())
    f_came_from, f_start, f_goal = a_star_search(new_tile, go_start, go_goal, mode)
    path_to_move(reconstruct_path(f_came_from, f_start, f_goal), new_tile)



if __name__=='__main__':
    main()

