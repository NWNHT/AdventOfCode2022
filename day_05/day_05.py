
from copy import deepcopy

def solution(filename: str):

    with open(filename, 'r') as fh:
        ipt = fh.readlines()

    # Parse the stacks
    num_stacks = len(ipt[0]) // 4
    stacks = [[] for _ in range(num_stacks)]
    for line in [line for line in ipt if '[' in line]:
        for i in range(num_stacks):
            stacks[i].append(None if line[i*4 + 1] == ' ' else line[i*4 + 1])
    stacks = [[x for x in lst if x is not None][::-1] for lst in stacks]
    print(stacks)
    
    # Parse the instructions
    instructions = []
    for line in [line for line in ipt if line[0] == 'm']:
        instructions.append([int(n) for n in line.split()[1:6:2]])

    # Make the moves
    stacks1 = deepcopy(stacks)
    stacks2 = stacks
    for i, inst in enumerate(instructions):
        CrateMover9000(stacks1, inst)
        CrateMover9001(stacks2, inst)

    return ''.join([l[-1] for l in stacks1]), ''.join([l[-1] for l in stacks2])
    

def CrateMover9000(stacks, inst):
    stacks[inst[2] - 1].extend(stacks[inst[1] - 1][-inst[0]:][::-1])
    del stacks[inst[1] - 1][-inst[0]:]
    

def CrateMover9001(stacks, inst):
    stacks[inst[2] - 1].extend(stacks[inst[1] - 1][-inst[0]:])
    del stacks[inst[1] - 1][-inst[0]:]


if __name__ == '__main__':
    p1, p2 = solution('input.txt')
    print(f"CrateMover9000: {p1}")
    print(f"CrateMover9001: {p2}")
