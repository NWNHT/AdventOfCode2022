
from math import floor

class Monkey:
    
    def __init__(self,p1, num, items, op, div, if_true, if_false) -> None:
        self.p1 = p1 # Part 1 vs Part 2 flag, controls dividing by 3

        self.num = num
        self.items = items
        self.op = op
        self.div = div
        self.common = 0
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def __str__(self) -> str:
        return f"Monkey {self.num}: {self.items}\n"
    
    def operation(self, item):
        # Perform custom operation, then divide by 3, then round down to integer
        op_result = eval(self.op)
        if self.p1: op_result = floor(op_result / 3)
        
        # Just big number things
        if not self.p1: op_result = op_result % self.common

        return op_result
    
    def target(self, item):
        # Return the target of the item, uses the divisor test
        return self.if_true if not (item % self.div) else self.if_false
    
    def inspect(self):
        # Inspect all items in monkey's inventory
        
        # A list of tuples (sink monkey, item)
        items_to_throw = []
        for item in self.items:
            self.inspections += 1
            op_item = self.operation(item)
            items_to_throw.append((self.target(op_item), op_item))
        
        # Clear inventory and send items to throw
        self.items = []
        return items_to_throw

    
class Barrel:
    
    def __init__(self) -> None:
        self.monkeys = [] 
        self.common = 1
    
    def collect_monkeys(self, text, p1):
        # Parse the monkey input text
        
        for monkey in text:
            num = int(monkey[0].split()[-1][:-1])
            items = [int(x) for x in monkey[1].replace(',', ' ').split()[2:]]
            op = monkey[2].split('=')[-1].replace('old', 'item')
            
            # This is used to calculate the common divisor
            test = int(monkey[3].split()[-1])
            self.common *= test

            if_true = int(monkey[4].split()[-1])
            if_false = int(monkey[5].split()[-1])

            self.monkeys.append(Monkey(p1, num, items, op, test, if_true, if_false))
        
        # Assign the common divisor to each of the monkeys
        for monkey in self.monkeys:
            monkey.common = self.common

    def __str__(self) -> str:
        out = ''
        for monkey in self.monkeys:
            out += f"Monkey {monkey.num}: {monkey.items}\n"
        return out

    def distribute(self, items):
        # Add the item to the list of the indicated monkey
        for item in items:
            self.monkeys[item[0]].items.append(item[1])

    def full_round(self):
        # For each monkey in list self.monkeys, call inspect, then call distribute
        for monkey in self.monkeys:
            self.distribute(monkey.inspect())
    
    def conduct_n_rounds(self, n, verbose=False):
        # Just call n rounds
        print(f"Starting Position")
        print(self)
        for i in range(n):
            self.full_round()
            if verbose and (i == 19 or not ((i + 1) % 1000)): 
                print(f"Round {i + 1} Results")
                self.monkey_business_summary()

        print(f"After round {i + 1}")
        print(self)
    
    def monkey_business_summary(self):

        print("Monkey Business:")
        for monkey in self.monkeys:
            print(f"Monkey {monkey.num}: {monkey.inspections}")
    
    def monkey_business_level(self):
        business = sorted([x.inspections for x in self.monkeys])
        return business[-2] * business[-1]


def solution(filename):

    with open(filename, 'r') as fh:
        monkeys = [[y.strip() for y in x.split('\n')] for x in fh.read().strip().split('\n\n')]
    
    # Part 1
    # Create barrel of monkeys and populate
    p1barrel = Barrel()
    p1barrel.collect_monkeys(monkeys, True)

    # Let 20 rounds pass
    p1barrel.conduct_n_rounds(20)
    
    # Get a summary of the monkey business
    p1barrel.monkey_business_summary()

    # Part 2
    print("\n\n Part 2\n\n")
    # Create barrel of monkeys and populate
    p2barrel = Barrel()
    p2barrel.collect_monkeys(monkeys, False)
    
    # Let 20 rounds pass
    p2barrel.conduct_n_rounds(10000, False)

    # Get a summary of the monkey business
    p2barrel.monkey_business_summary()

    print(f"Part 1 monkey business level: {p1barrel.monkey_business_level()}")
    print(f"Part 2 monkey business level: {p2barrel.monkey_business_level()}")

if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
