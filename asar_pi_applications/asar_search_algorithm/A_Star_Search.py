from queue import PriorityQueue
import asar_search_algorithm.Pi_Cfg as CONFIG
import base64
import logging

with open('search.log', 'w'):
    pass
logging.basicConfig(filename='search.log', level=logging.INFO)

log = logging.getLogger(__name__)

TERRAIN_HEIGHT = CONFIG.TERRAIN_HEIGHT  # number of tiles down the side
TERRAIN_WIDTH = CONFIG.TERRAIN_WIDTH   # number of tiles across the top

INFINITY = CONFIG.INFINITY   # variable representing impassable terrain

filename = 'terrain.txt'


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


# instantiates the dictionary of tiles with its coordinates and attributes
def instantiate_graph():
    tile = {}

    for x in range(1, TERRAIN_HEIGHT+1):
        for y in range(1, TERRAIN_WIDTH+1):
            attribute = {}  # prevents the list from overwriting old dictionary keys
            if x % 2 == 0:  # x is even
                temp_child = [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x, y+1), (x-1, y)]
            else:
                temp_child = [(x, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y)]

            # remove neighbor nodes that are out of grid
            children = filter(lambda i: 1 <= i[0] <= TERRAIN_HEIGHT and 1 <= i[1] <= TERRAIN_WIDTH, temp_child)
            attribute['children'] = list(children)
            attribute['immediate_danger'] = 0
            attribute['adjacent_danger'] = 0
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
        current = frontier.get()  # pulls the least expensive node off of queue

        if current == goal:  # goal test
            log.info('Goal Reached!')
            break

        for i in range(0, len(tile[current]['children'])):
            next = tile[current]['children'][i]  # iterates through children of current node
            if tile[next] == goal:
                priority = cost_so_far[current] + 1 + CONFIG.heuristic(goal, next, tile)
                frontier.put(next, priority)
                came_from[next] = current
                break
            else:
                # heuristic part 1 (uses danger & Speed)
                new_cost = cost_so_far[current] + CONFIG.travel(current, next, tile, mode)
                if next not in cost_so_far or new_cost < cost_so_far[next]:  # if next has not been visited
                    if tile[next]['speed'] < INFINITY:  # do not evaluate obstacles (Rock & water)
                        # do not drive through fire in safe mode
                        if mode == 0 and tile[next]['immediate_danger'] >= CONFIG.SAFE_LIMIT:
                            continue
                        else:
                            cost_so_far[next] = new_cost
                            # heuristic part 2 (Euclidean distance)
                            priority = new_cost + CONFIG.heuristic(goal, next, tile, mode)
                            log.info('{0} --> {1} = {2}'.format(current, next, priority))
                            frontier.put(next, priority)  # put evaluated node onto queue
                            came_from[next] = current

    return came_from, start, goal


# Reconstruct_path pulls the path from the queue
def reconstruct_path(came_from, start, goal):
    current = goal
    if current not in came_from:
        raise ValueError('No drivable path')

    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional

    return path  # This is the final output path to be sent to the vision system for the path overlay on the image


def print_path(path):

    log.info(path)

    row = {}

    for i in range(8):
        if i % 2 == 0:  # even
            row[i] = ['  x', '  x', '  x', '  x', '  x', '  x', '  x', '  x']
        else:
            row[i] = ['x  ', 'x  ', 'x  ', 'x  ', 'x  ', 'x  ', 'x  ', 'x  ']

    for index, item in enumerate(path):
        for i in range(8):
            for j in range(8):
                if path[index] == (i+1, j+1) and i % 2 == 0:  # even
                    row[i][j] = '  O'
                elif path[index] == (i+1, j+1) and i % 2 != 0:  # odd
                    row[i][j] = 'O  '

    for i in range(8):
        log.info(' '.join(row[i]))


# path_to_move converts the path from coordinates to the robot's instruction protocol
def path_to_move(path, tile, orientation):

    if path == -1:
        raise ValueError('No path to convert to instructions')

    movement = []  # list of robot instructions

    # orientation = cfg.orientation  # import exact orientation from vision system (current orientation variable)

    for i in range(1, len(path)):

        # convert heuristic speed to hex speed
        if tile[path[i]]['speed'] == 0:  # fast
            speed = CONFIG.FAST
        elif tile[path[i]]['speed'] == 1:  # medium
            speed = CONFIG.MEDIUM
        else:  # default speed for unknown objects == slow
            speed = CONFIG.SLOW

        # choose appropriate relative angle to turn based on current orientation and relative position of next tile
        if path[i-1][0] % 2 == 0:  # tile's row is even
            if path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:  # move up && right
                turn = 60 - orientation
                orientation = 60
            elif path[i][0] < path[i-1][0] and path[i][1] < path[i-1][1]:  # move up && left
                turn = 120 - orientation
                orientation = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:  # move left
                turn = 180 - orientation
                orientation = 180
            elif path[i][0] > path[i-1][0] and path[i][1] < path[i-1][1]:  # move down && left
                turn = orientation + 120
                orientation = -120
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:  # move down && right
                turn = orientation + 60
                orientation = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:  # move right
                turn = 0 - orientation
                orientation = 0
            else:  # default no move
                turn = 0
                speed = 0
        else:  # tile's row is odd
            if path[i][0] < path[i-1][0] and path[i][1] > path[i-1][1]:  # move up && right
                turn = 60 - orientation
                orientation = 60
            elif path[i][0] < path[i-1][0] and path[i][1] == path[i-1][1]:  # move up && left
                turn = 120 - orientation
                orientation = 120
            elif path[i][0] == path[i-1][0] and path[i][1] < path[i-1][1]:  # move left
                turn = 180 - orientation
                orientation = 180
            elif path[i][0] > path[i-1][0] and path[i][1] == path[i-1][1]:  # move down && left
                turn = orientation + 120
                orientation = -120
            elif path[i][0] > path[i-1][0] and path[i][1] > path[i-1][1]:  # move down && right
                turn = orientation + 60
                orientation = -60
            elif path[i][0] == path[i-1][0] and path[i][1] > path[i-1][1]:  # move right
                turn = 0 - orientation
                orientation = 0
            else:  # default no move
                turn = 0
                speed = 0

        # convert the angles (in degrees) to their unit circle equivalents that are under 255 degrees
        if turn == 300:  # 300 degrees == -60 degrees
            turn = -60
        elif turn == 240:  # 240 degrees == -120 degrees
            turn = -120

        # identify positive/negative rotation
        if turn > 0:
            rotation = 'AA'  # rotate left
        else:
            rotation = 'BB'  # rotate right

        # add a turn + drive instruction to list of movements
        if turn == 0:
            movement.append('FFCC28{0}F0'.format(speed))
        else:
            movement.append('FF{0}{1}F0'.format(rotation, format(abs(turn), '02X')))
            movement.append('FFCC28{0}F0'.format(speed))

    movement.append('FFFFFF')  # end transmission

    trail = ''.join(movement)  # convert transmission list to string

    for i in range(0, len(movement)):  # optional vertical display of instructions
        log.info(movement[i])

    # log.info(trail)

    binary_trail = base64.b16decode(trail)

    # log.info(binary_trail)

    return binary_trail


def runSearch(terrain_path, mode):
    start, goal, tile, orientation = CONFIG.give_danger(instantiate_graph(), terrain_path)
    came_from, start, goal = a_star_search(tile, start, goal, mode)
    coordinate_path = reconstruct_path(came_from, start, goal)
    robot_instructions = path_to_move(coordinate_path, tile, orientation)
    print_path(coordinate_path)
    return robot_instructions, coordinate_path, start, goal


def main():
    runSearch('terrain.txt', 0)  # 0 for safe, 1 for smart, 2 for fast, 3 for direct
    input()
    runSearch('terrain.txt', 1)
    input()
    runSearch('terrain.txt', 2)
    input()
    runSearch('terrain1.txt', 3)


if __name__ == '__main__':
    main()
