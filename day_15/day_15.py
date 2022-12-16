from tqdm import tqdm

class BeaconSensor:
    def __init__(self, sx, sy, x, y) -> None:
        self.sx = sx
        self.sy = sy

        self.x = x
        self.y = y

        self.distance = abs(x - sx) + abs(y - sy)
    
    @property
    def beacon(self):
        return (self.x, self.y)
    
    @property
    def sensor(self):
        return (self.sx, self.sy)
    
    def __repr__(self) -> str:
        return f"B: ({self.x}, {self.y}) S: ({self.sx}, {self.sy}), D: {self.distance}"
    
    def project(self, target):
        # if the y value of the sensor is within distance of the target then make projection
        a = self.distance - abs(target - self.sy) # a is the manhatten distance left for x
        # if a > 0:
        self.seg = (self.sx - a, self.sx + a) if a > 0 else None
        return self.seg
    

class Cave:
    def __init__(self):
        self.beacons = []
    
    def add_beacon(self, x, y, sx, sy):
        self.beacons.append(BeaconSensor(x, y, sx, sy))
    
    def __repr__(self) -> str:
        out = ''
        for b in self.beacons:
            out += str(b) + '\n'
        return out
    
    def gen_project_segs(self, target):
        # Collect the segments of all of the beacons
        self.segs = []
        for beacon in self.beacons:
            seg = beacon.project(target)
            if seg is not None:
                self.segs.append(seg)
        return self.segs
        
    def target_coverage(self, target):
        self.gen_project_segs(target)

        coverage = set()
        for x in self.segs:
            coverage.update(list(range(x[0], x[1] + 1)))

        return len(coverage)
    
    def open_space(self, max_target):

        for l in tqdm(range(max_target)):

            self.gen_project_segs(l)
            self.segs = sorted(self.segs)
            start, end = self.segs[0]

            for i in range(len(self.segs)):
                new_start, new_end = self.segs[i]
                if new_end > max_target or start > max_target: break # The slightest bit of efficiency
                if end < new_start:
                    return end + 1, l
                else:
                    end = max(end, new_end)
            

def solution(filename):

    # Read the input
    with open(filename, 'r') as fh:
        ipt = [x.strip().split() for x in fh.readlines()]
        ipt = [(int(x[2].split('=')[-1][:-1]), int(x[3].split('=')[-1][:-1]), int(x[8].split('=')[-1][:-1]), int(x[9].split('=')[-1])) for x in ipt]
    
    # Build the cave with beacons and sensors
    cave = Cave()
    for pair in ipt:
        cave.add_beacon(*pair)
    
    # I originally wrote part 1 by just brute forcing checking the entire row but I later rewrote it to use the segments
    # Part 1
    coverage = cave.target_coverage(2000000)
    print(f"Not beacon a beacon including the existing beacon: {coverage}")
    print(f"Not beacon excluding existing beacon: {coverage - 1}") # This isn't brilliant but I can't be bothered

    # I had difficulties with this one
    # Part 2
    rx, ry = cave.open_space(4000000)
    print(f"The coordinates: ({rx}, {ry}) The tuning frequency: {ry + rx * 4000000}")

    
if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
