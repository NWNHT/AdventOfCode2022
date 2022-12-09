
from copy import deepcopy

def solution(filename):
    
    with open(filename, 'r') as fh:
        # ipt = [x.strip() for x in fh.readlines()]
        ipt = [[int(c) for c in x.strip()] for x in fh.readlines()]
    
    # Part 1
    # Create the mask, find visible for rows
    mask = [[0 for _ in range(len(ipt[0]))] for _ in range(len(ipt))]
    mask = find_visible(ipt, mask)
    # Transpose the matrix and find visible for rows again
    ipt_T = transpose(ipt)
    mask = transpose(mask)
    mask = find_visible(ipt_T, mask)
    print(f"The number of visible trees: {sum(map(sum, mask)) + 4}")

    # Part 2
    # Create new mask, find score, print
    mask = [[0 for _ in range(len(ipt[0]))] for _ in range(len(ipt))]
    mask = find_score(ipt, mask)
    print(f"Maximum Score: {max([max(x) for x in mask])}")


def find_visible(ipt, mask) -> int:
    # For each row, move 'inward' from both sides marking visible from each perspective
    for i in range(1, len(ipt) - 1): # for each of the rows
        largest_left = -1
        largest_right = -1
        
        for j in range(len(ipt[i])):
            if ipt[i][j] > largest_left:
                mask[i][j] = 1
                largest_left = ipt[i][j]
            if ipt[i][-(j + 1)] > largest_right:
                mask[i][-(j + 1)] = 1
                largest_right = ipt[i][-(j + 1)]
    
    return mask


def find_score(ipt, mask) -> int:
    # For each inner tree, check in all four directions for number of visible trees
    # off-by-one errors abound
    for i in range(1, len(ipt) - 1):
        for j in range(1, len(ipt[0]) - 1):
            running = 1
            count_ = 1
            for k in range(1, j):
                if ipt[i][j - k] < ipt[i][j]:
                    count_ += 1
                else:
                    break
            running *= count_

            count_ = 1
            for k in range(1, len(ipt[0]) - j - 1):
                if ipt[i][j + k] < ipt[i][j]:
                    count_ += 1
                else:
                    break
            running *= count_
            
            count_ = 1
            for k in range(1, i):
                if ipt[i - k][j] < ipt[i][j]:
                    count_ += 1
                else:
                    break
            running *= count_

            count_ = 1
            for k in range(1, len(ipt) - i - 1):
                if ipt[i + k][j] < ipt[i][j]:
                    count_ += 1
                else:
                    break
            running *= count_
            mask[i][j] = running
    
    return mask
                
    

def transpose(mat):
    return list(map(list, zip(*mat)))
    

if __name__ == '__main__':
    test = 'test_input.txt'
    test2 = 'test2_input.txt'
    data = 'input.txt'
    solution(data)
