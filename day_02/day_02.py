
def solution(filename: str):
    """Solution using dict and modulus, though I do appreciate the lookup table method"""

    dct = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    with open(filename, 'r') as fh:
        ipt = [[dct[x[0]] for x in y.split(' ')] for y in fh.readlines()]
    
    score_1 = score_2 = 0
    for line in ipt:
        # Problem 1
        score_1 += line[1] + 1 # Score for symbol
        score_1 += ((line[1] - (line[0] + 1) % 3 - 1) % 3) * 3 # Score for result

        # Problem 2
        score_2 += line[1] * 3 # Score for result
        score_2 += (line[0] + (line[1] - 1)) % 3 + 1 # Score for symbol

    return score_1, score_2

if __name__ == '__main__':

    filename = 'input.txt'
    p1, p2 = solution(filename=filename)
    print(f"Problem 1: {p1}\nProblem 2: {p2}")
 