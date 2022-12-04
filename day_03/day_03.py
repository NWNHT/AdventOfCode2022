
def solution(filename: str):
    """Find 'common' characters using sets and intersections"""

    def l2a(c):
        """Get value from char"""
        if ord(c) >= ord('a'):
            return ord(c) - ord('a') + 1
        else:
            return ord(c) - ord('A') + 1 + 26
    
    with open(filename, 'r') as fh:
        ipt = [x.strip() for x in fh.readlines()]
    
    score1 = 0
    for line in ipt:
        overlap = list(set(line[:(len(line)//2)]).intersection(set(line[int(len(line)//2):])))[0]
        score1 += l2a(overlap)
    
    score2 = 0
    for i in range(0, len(ipt), 3):
        overlap = list(set(ipt[i]).intersection(set(ipt[i + 1]).intersection(set(ipt[i + 2]))))[0]
        score2 += l2a(overlap)
    
    return score1, score2

if __name__ == '__main__':
    p1, p2 = solution('input.txt')
    print(f"Sum of priorities: {p1}\nSum of priorities: {p2}")
