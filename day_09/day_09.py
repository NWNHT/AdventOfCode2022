
class Rope:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.history = [(0, 0)]

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

        self.history.append((self.x, self.y))

class Head(Rope):

    def __init__(self):
        self.next_move = None
        super().__init__()
    
    def set_next_move(self, direction):
        self.next_move = direction

    def tick(self):
        # move the position in the given direction the given number of times
        if self.next_move == 'U':
            self.y += 1
        elif self.next_move == 'D':
            self.y -= 1
        elif self.next_move == 'R':
            self.x += 1
        elif self.next_move == 'L':
            self.x -= 1
        else:
            print(f"Error moving, given: {self.next_move}")
        
        self.history.append((self.x, self.y))
        
        return (self.x, self.y)

    
class Knot(Rope):
    def __init__(self, follows = None):
        super().__init__()
        self.follows = follows
    
    def set_follows(self, follows):
        self.follows = follows

    def tick(self):
        if (abs(self.follows.x - self.x) > 1) and (abs(self.follows.y - self.y) > 1): # If diagonal off
            x_move = int((self.follows.x - self.x)/abs(self.follows.x - self.x))
            y_move = int((self.follows.y - self.y)/abs(self.follows.y - self.y))
            self.move_to(x=self.x + x_move, y=self.y + y_move)
        elif (abs(self.follows.x - self.x) > 1):
            x_move = int((self.follows.x - self.x)/abs(self.follows.x - self.x))
            self.move_to(x=self.x + x_move, y=self.follows.y)
        elif (abs(self.follows.y - self.y) > 1):
            y_move = int((self.follows.y - self.y)/abs(self.follows.y - self.y))
            self.move_to(x=self.follows.x, y=self.y + y_move)
        else:
            # The tail is close to the head, do nothing
            pass

        
def part1(ipt, loud: bool=False, draw_grid: bool=False):
    head = Head()
    tail = Knot(follows=head)

    for inst in ipt:
        if loud: print(f"\nMoving head: {inst[0]} : {inst[1]}")
        for _ in range(int(inst[1])):
            # Make the head move
            head.set_next_move(inst[0])
            head.tick()

            # Make the tail move
            tail.tick()

            if loud: print(f"Summary: head: {head}, tail: {tail}, diff: ({head.x - tail.x}, {head.y - tail.y})")
            if draw_grid: draw(rope=[head, tail])
    
    print(f"The number of unique tail positions is: {len(set(tail.history))}")


def draw(rope, size: int = 6):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for i, knot in reversed(list(enumerate(rope))):
        grid[size - knot.y - 1][knot.x] = i
    
    for row in grid:
        print(*row)


def part2(ipt):

    # Create rope
    rope = [Head(), *([Knot() for _ in range(9)])]
    
    # Link all of the knots
    for i, knot in enumerate(rope):
        if isinstance(knot, Knot):
            knot.set_follows(rope[i - 1])
        
    # For each instruction, set to head, and then update each knot
    for inst in ipt:
        for _ in range(int(inst[1])):
            rope[0].set_next_move(inst[0])
            
            for knot in rope:
                knot.tick()

    print(f"The number of unique tail posisions is: {len(set(rope[-1].history))}")
    
        
def solution(filename):
    with open(filename, 'r') as fh:
        ipt = [x.strip().split() for x in fh.readlines()]
    
    # Part 1
    part1(ipt)

    # Part 2
    part2(ipt)

    
if __name__ == '__main__':
    test = 'test_input.txt'
    test2 = 'test2_input.txt'
    data = 'input.txt'
    solution(data)
