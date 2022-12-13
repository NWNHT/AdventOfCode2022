
from time import perf_counter

def get_start(grid, level) -> tuple:
    # Get the indices of the node with the specified value
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == level:
                return (i, j)


def get_around(grid, x, y):
    # Generate list of nodes adjacent to given node
    return [i for i in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if (i[0] < len(grid)) and (i[0] > -1) and (i[1] < len(grid[0])) and (i[1] > -1)]


def paths(node, start, parents):
    # Generate a list of the visited nodes
    path = [node]
    while path[-1] != start:
        path.append(parents[path[-1]])
    return path
    

def bfs(grid, start, end, condition):
    # Conduct a bfs

    queue_ = [start]
    explored = []
    parents = {}

    while(len(queue_)):

        # Get the next node
        (x, y) = queue_.pop(0)

        # Check if the right node
        if grid[x][y] == end:
            return paths((x, y), start, parents)

        # For each adjacent node if not explored and able to explore then add to queue and explored lists, note the parent
        for node in get_around(grid, x, y):
            if (node not in explored) and condition(grid[x][y], grid[node[0]][node[1]]):
                parents[node] = (x, y)
                explored.append(node)
                queue_.append(node)


def dijkstra(grid, start, end, condition):
    # Same as above but dijkstra
    
    queue_ = [(0, start)]
    explored = []

    while(len(queue_)):
        
        # Get the next node, the lowest value node will always be at the beginning of the queue
        (weight, (x, y)) = queue_.pop(0)

        if grid[x][y] == end:
            return weight
        
        for node in get_around(grid, x, y):
            if (node not in explored) and condition(grid[x][y], grid[node[0]][node[1]]):
                explored.append(node)
                queue_.append((weight + 1, node))
    

def solution(filename):
    
    with open(filename, 'r') as fh:
        ipt = [[ord(y) - ord('a') + 1 for y in x.strip().replace('E', '{')] for x in fh.readlines()]
    
    # Part 1
    def search_for_E(a, b):
        return a + 1 >= b

    start = get_start(ipt, -13)
    ipt[start[0]][start[1]] = 1
    print(f"The shortest path to the peak from S is {len(bfs(ipt, start, 27, search_for_E)) - 1} steps long.")
    print(f"The shortest path to the peak from S is {dijkstra(ipt, start, 27, search_for_E)} steps long.")

    # Part 2
    def search_for_a(a, b):
        return b + 1 >= a
    
    start = get_start(ipt, 27)
    print(f"The shortest path to the peak from any 'a' is {len(bfs(ipt, start, 1, search_for_a)) - 1} steps long.")
    print(f"The shortest path to the peak from any 'a' is {dijkstra(ipt, start, 1, search_for_a)} steps long.")

if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
