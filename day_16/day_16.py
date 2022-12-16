
import re

class Valve:
    def __init__(self, name, flow, tunnels) -> None:
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        self.open = False
        self.distances = None

    def __repr__(self) -> str:
        return f"{self.name} - {str(self.flow).zfill(2)} - {self.tunnels}"
    
    def get_distances(self, valves):
        self.distances = get_distances(valves, self.name)

            
def get_distances(valves, perspective):
    # Do a dijkstra search, every branch has weight 1
    
    explored = [perspective]
    scores = {perspective: 1}
    queue = [perspective]

    while(len(queue)):
        node = queue.pop(0)
        for i in valves[node].tunnels:
            if i not in explored:
                queue.append(i)                # Add to queue
                explored.append(i)             # Add to explored list
                scores[i] = scores[node] + 1   # Note the score

    return scores


def find_max_pressure(valves, curr, opened, useful, time=1, max_time = 30):
    # print(opened)

    max_pressure = 0
    for valve_id in useful:

        # If the valve has already been opened the ignore
        if valve_id in opened:
            continue
        # If the distance to the valve exceeds the time limit then ignore
        if valves[curr].distances[valve_id] > (max_time - time):
            continue

        # Calculate the score it would add
        score = (max_time - time - valves[curr].distances[valve_id]) * valves[valve_id].flow

        # Recursively call this function to determine the next best move
        max_pressure = max(max_pressure, score + find_max_pressure(valves, valve_id, opened + [valve_id], useful, time + valves[curr].distances[valve_id], max_time))
    
    # print(max_pressure)
    return max_pressure


def solution(filename):

    # Reading data
    patt = re.compile(r'Valve (..) has flow rate=(\d*); tunnel[s]? lead[s]? to valve[s]? (.*)')
    with open(filename, 'r') as fh:
        ipt = [(x[0], x[1], [y.strip(', ') for y in x[2].split()]) for x in patt.findall(fh.read())]
    valves = {}
    for i in ipt:
        # Create a valve and put it in dictionary by valve name
        valves[i[0]] = Valve(i[0], int(i[1]), i[2])
    
    # Generate the distances for each of the nodes
    for i in valves.values():
        i.get_distances(valves)
    
    # Part 1
    # Prune the nodes/valves to check down to the list of useful ones
    useful = [x.name for x in valves.values() if x.flow > 0]
    # Set the maximum time
    max_time = 30
    # Set the starting position
    current = 'AA'
    print(f"The maximum pressure release-able is: {find_max_pressure(valves, current, [], useful, 0, max_time)}")

    # Part 2
    # Now there are only 26 minutes, 
    # Idea: Go through the same optimize thing, but have two options to proceed
    # - for each of the person and elephant that is waiting
    # Loop through the time left
    # If the person is not busy, then give one off list
    # If the elephant is not busy, then give one off list
    # Then go into the recursion 
    # ???
    # Profit


if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(test)