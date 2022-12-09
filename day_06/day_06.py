
def solution(filename: str):
    
    with open(filename, 'r') as fh:
        ipt = fh.readline().strip()
    
    for i in range(len(ipt)):
        if len(set(ipt[i-4:i])) == 4:
            marker1 = i
            break
    
    for i in range(len(ipt)):
        if len(set(ipt[i-14:i])) == 14:
            return marker1, i


if __name__ == '__main__':
    p1, p2 = solution('input.txt')
    print(f"Packet Marker: {p1}\nMessage Marker: {p2}")
