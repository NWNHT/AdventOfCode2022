
from copy import deepcopy

def update(cave, x, y, fill):
    # Update given point with given symbol
    cave[x][y] = fill


def rockline(cave, co1, co2):
    # Print a line of rocks, conditional here instead of sorting by size

    if (co1[0] <= co2[0]) and (co1[1] <= co2[1]):
        for x in range(co2[0] - co1[0] + 1):
            for y in range(co2[1] - co1[1] + 1):
                update(cave, co1[0] + x, co1[1] + y, '#')
    else:
        for x in range(co1[0] - co2[0] + 1):
            for y in range(co1[1] - co2[1] + 1):
                update(cave, co2[0] + x, co2[1] + y, '#')


def build_cave_part_1(ipt):
    # Build the cave for part 1

    # Create the blank cave
    all_x = [y[0] for x in ipt for y in x]
    all_y = [y[1] for x in ipt for y in x]
    cave = [['.' for _ in range(0, max(all_y) + 1)] for _ in range(min(all_x), max(all_x) + 1)]

    # Shift all of the inputs based on the width of the cave required
    ipt = deepcopy(ipt)
    for line in ipt:
        for coord in line:
            coord[0] = coord[0] - min(all_x)
    sand = [500 - min(all_x), 0]

    # Draw the rocks in the cave
    for line in ipt:
        for i in range(len(line) - 1):
            rockline(cave, line[i], line[i + 1])
    
    return cave, sand


def build_cave_part_2(ipt):
    # Build the cave for part 2
    
    # Create the blank cave
    all_y = [y[1] for x in ipt for y in x]
    max_y = max(all_y)
    cave_height = max_y + 1 + 2 * (1) 
    cave_width = 1 + 2 * (max_y + 2)
    cave = [['.' for _ in range(0, cave_height)] for _ in range(cave_width)]

    # Shift all of the inputs based on width of the cave required
    for line in ipt:
        for coord in line:
            coord[0] = int(coord[0] - (500 - ((cave_width - 1) / 2)))
    sand = [int(((cave_width - 1) / 2)), 0]

    # Draw the rocks in the cave
    for line in ipt:
        for i in range(len(line) - 1):
            rockline(cave, line[i], line[i + 1])
    
    # Draw the bottom rockline
    rockline(cave, [0, cave_height - 1], [cave_width - 1, cave_height - 1])
    
    return cave, ipt, sand
    
            
def print_cave(cave):
    # Print the first element of each row of cave, for the length of the rows of caves
    for i in range(len(cave[0])):
        print(str(i).zfill(3), end=' ')
        for col in cave:
            print(col[i], end='')
        print('')


def part_1(cave, sand, verbose: bool=False):
    index = deepcopy(sand)
    cave = deepcopy(cave)
    count = 0
    if verbose: print_cave(cave)
    while(1):
        if index[1] == (len(cave[0]) - 1): # If the sand is in the final row then break
            break
        if cave[index[0]][index[1] + 1] == '.':
            index = [index[0], index[1] + 1]
        elif cave[index[0] - 1][index[1] + 1] == '.':
            index = [index[0] - 1, index[1] + 1]
        elif cave[index[0] + 1][index[1] + 1] == '.':
            index = [index[0] + 1, index[1] + 1]
        else: # If no place can be found then count and make new piece of sand
            count += 1
            update(cave, index[0], index[1], 'o')
            index = deepcopy(sand)

    # Print the result
    if verbose: print_cave(cave)
    print(f"{count} pieces of sand came to rest.")


def part_2(cave, sand, verbose: bool=False):
    index = deepcopy(sand)
    cave = deepcopy(cave)
    count = 0
    if verbose: print_cave(cave)
    while(1):
        if cave[index[0]][index[1] + 1] == '.':
            index = [index[0], index[1] + 1]
        elif cave[index[0] - 1][index[1] + 1] == '.':
            index = [index[0] - 1, index[1] + 1]
        elif cave[index[0] + 1][index[1] + 1] == '.':
            index = [index[0] + 1, index[1] + 1]
        else: # If no place can be found then count and break if at sand source, else make new sand
            count += 1
            if index == sand:
                break
            update(cave, index[0], index[1], 'o')
            index = deepcopy(sand)

    # Print the result
    if verbose: print_cave(cave)
    print(f"{count} pieces of sand came to rest.")


def solution(filename):
    
    with open(filename, 'r') as fh:
        ipt = [[[int(z) for z in y.split(',')] for y in x.strip().replace(' -> ', ' ').split()] for x in fh.readlines()]
    
    # Build the Part 1 cave
    cave, sand = build_cave_part_1(ipt)

    # Complete Part 1
    part_1(cave, sand)

    # Build the Part 2 cave
    cave, ipt2, sand = build_cave_part_2(ipt)

    # Complete Part 2
    part_2(cave, sand)


if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
