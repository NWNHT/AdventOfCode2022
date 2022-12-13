
from functools import cmp_to_key

def analyze_pair(left, right, verbose: bool=False):
    # Takes two items and compares them recursively
    # Returns 1 if left is less than right, 0 if equal, and -1 if right is less than left

    if isinstance(left, int) and isinstance(right, int):
        if verbose: print(f"Both are int")
        if left < right:
            return -1
        elif right < left:
            return 1
        else:
            return 0
    
    if isinstance(left, list) and isinstance(right, list):
        if verbose: print(f"Both are list")
        if len(left) == 0 and len(right) == 0:
            pass
        for i in range(max(len(left), len(right))):
            # Check to make sure neither is empty
            if i == len(left):
                return -1
            elif i == len(right):
                return 1
            
            # Recursively call function on the first elements
            if verbose: print(f"Calling analyze_pair on {left[i]} and {right[i]}")
            result = analyze_pair(left[i], right[i], verbose)
            if result:
                return result
            
    if isinstance(left, list) and isinstance(right, int):
        if verbose: print(f"left is list, right is int")
        result = analyze_pair(left, [right], verbose)
        if result:
            return result
    
    if isinstance(left, int) and isinstance(right, list):
        if verbose: print(f"left is int, right is list")
        result = analyze_pair([left], right, verbose)
        if result:
            return result
    
    return 0

            
def solution(filename):
    
    with open(filename, 'r') as fh:
        ipt = [[eval(y) for y in x.strip().split('\n')] for x in fh.read().split('\n\n')]
    

    # Part 1
    sum_ = 0
    # Loop through the pairs and sum indices of pairs in correct order
    verbose = False
    for i, pair in enumerate(ipt):
        result = analyze_pair(pair[0], pair[1], verbose)
        if result == -1:
            if verbose: print(f"Pair {i} is valid")
            sum_ += i + 1
        elif result == 1:
            if verbose: print(f"Pair {i} is invalid")
    
    print(f"The sum of the indices of the valid pairs is: {sum_}")


    # Part 2
    # Modify input format to be a single list of packets
    ipt_part_2 = [item for x in ipt for item in x]
    ipt_part_2.extend([[[2]], [[6]]])

    # Use Python's built in sorting with a custom comparison function and functools cmp_to_key function
    ipt_part_2.sort(key=cmp_to_key(analyze_pair))

    # Find the two special packets and print
    first = ipt_part_2.index([[2]]) + 1
    second = ipt_part_2.index([[6]]) + 1
    print(f"The decoder key is: {first * second}")

    
if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
