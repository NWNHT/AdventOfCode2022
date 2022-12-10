
def solution(filename):
    
    with open(filename, 'r') as fh:
        ipt = iter([x.strip() for x in fh.readlines()])
    
    # Initialize the system
    cycle = 1
    to_add = 0
    X = 1
    x_register = []

    # Just read instructions until there are none left
    while(1):

        # If there is something to add from a previous instruction then that takes priority, it is added after the log of the register is saved
        # - This is effectively between cycles
        if to_add:
            x_register.append((cycle, X))

            X += to_add
            to_add = 0
        else:
            # Get next command, exit if none left
            try:
                inst = next(ipt)
            except StopIteration:
                break

            # If it is a noop then just continue to increment cycle, else place number in to_add buffer to be applied at the end of the next cycle
            if inst == 'noop':
                pass
            else:
                to_add = int(inst.split()[-1])
            
            x_register.append((cycle, X))
        
        cycle += 1

    # Just sum the product of register and cycle values at the given indices: 20, 60, 100, ...
    print(f"The sum of the selected cycle signal strengths is: {sum([x_register[i - 1][1] * i for i in range(20, len(x_register), 40)])}")

    # Draw the screen
    draw(x_register)
        

def draw(register):

    # For each cycle, check if the 3 wide sprite overlaps with the cycle mod 40, note the '-1' because of how the cycles begin on 1, not 0
    for (cycle, x) in register:
        if ((cycle - 1) % 40) - x in [-1, 0, 1]:
            print('#', end='')
        else:
            print(' ', end='') # replaced '.' with ' '
        if not cycle % 40:
            print('')


if __name__ == '__main__':
    test = 'test_input.txt'
    stest = 'small_test.txt'
    s2test = 'small_test2.txt'
    data = 'input.txt'
    solution(data)
