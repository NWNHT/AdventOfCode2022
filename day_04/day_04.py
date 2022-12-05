
def solution(filename: str):
    with open(filename, 'r') as fh:
        # Yikes with four list comprehensions in a single line to create list of values [L1, H1, L2, H2] from 'L1-H1,L2-H2'
        ipt = [[*[int(z) for z in y[0].split('-')], *[int(z) for z in y[1].split('-')]] for y in [x.strip().split(',') for x in fh.readlines()]]

    score1 = 0
    for line in ipt:
        # Checking if the min and max of one range are less/greater(respectively) than the other range
        # Some cooler math could be done if it was 'strictly contains' instead of 'contains including the limit'
        # - Then for range 'L1-H1,L2-H2' the product (H2 - H1) * (L2 - L1) would always be negative when 'containing'
        # - Something similar could be implemented here by adding/subtracting 1 from the ranges but it gets messier than this solution
        if line[0] <= line[2] and line[1] >= line[3]:
            score1 += 1
        elif line[0] >= line[2] and line[1] <= line[3]:
            score1 += 1
    
    score2 = 0
    for line in ipt:    
        # Just have to check that the maximum of one range doesn't equal or exceed the minimum of the other, using inverse logic
        if not (line[1] < line[2] or line[3] < line[0]):
            score2 += 1
             
    return score1, score2
    
if __name__ == '__main__':
    p1, p2 = solution('input.txt')
    print(f"Total 'contain's: {p1}\nTotal 'overlap's: {p2}")
