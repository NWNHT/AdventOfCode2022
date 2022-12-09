
class Node:
    """Node class/structure for the file system
    """

    def __init__(self, parent, name, children: list=None, size: int=0, dir_: bool=False):
        self.parent = parent
        self.children = children or []
        self.size = size
        self.name = name
        self.path = '/' if parent is None else parent.path + '/' + name
        self.dir_ = dir_
    
    def __str__(self) -> str:
        return f"Name: {self.name}\n  Path: {self.path}\n  Size: {self.size}\n  Children: {self.children}"
    
    def add_size(self, size: int):
        """Recursively add size of file to self and any parents

        Args:
            size (int): The size of the file
        """
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)
    
    def print_tree(self):
        """Print the entire tree from this node 'down'
        """
        # Print this node, then print the nodes of children,
        print(str('  '*(self.path.count('/') - 1)) + '-' + f"{self.name} ({self.size}{' - dir' if self.dir_ else ''})")

        # Print this node
        for child in self.children:
            child.print_tree()

    def dirs_lte_gte_n(self, n: int, lte: bool):
        """Recursive method to find all directories in a node that are lte or gte a given value

        Args:
            n (int): The threshold
            lte (bool): Boolean for lte/gte, True for lte, False for gte

        Returns:
            List[Node]: A list of nodes of directories that meet the threshold condition
        """

        if self.dir_:
            if lte:
                if self.size <= n:
                    lst = [self]
                else:
                    lst = []
            else:
                if self.size >= n:
                    lst = [self]
                else:
                    lst = []
                

            for child in self.children:
                lst.extend(child.dirs_lte_gte_n(n=n, lte=lte))

            return lst

        return []
    
    def sum_dirs_under_100000(self) -> int:
        """Specifically for p1

        Returns:
            int: The sum of all of the directories smaller than 100000 in size
        """

        lst = self.dirs_lte_gte_n(n=100000, lte=True)
        sum_ = 0
        for node in lst:
            sum_ += node.size
        
        return sum_
    
    def smallest_above_threshold(self, threshold: int) -> int:
        """Specifically for p2

        Args:
            threshold (int): The threshold that the directory must be larger than

        Returns:
            smallest: The smallest directory above the given threshold
        """

        lst = self.dirs_lte_gte_n(n=threshold, lte=False)

        smallest = 30_000_000
        for node in lst:
            if node.size < smallest: smallest = node.size

        return smallest
        

def construct_tree(ipt):
    """Given list of lines, create a root node and tree from reading the file system

    Args:
        ipt (List[str]): List of strings to be read as input for the tree

    Returns:
        (Node): The root node that resulted from the inputs
    """
    
    root = Node(parent=None, name='root', dir_ = True)
    cursor = root
    for line in ipt:
        # I wish all Python has switch cases
        if line[0] == 'dir': # If a directory is found
            cursor.children.append(Node(parent=cursor, name=line[1], dir_=True))
        elif line[0] == '$' and line[1] == 'cd': # If a cd is found
            if line[2] == '..':
                cursor = cursor.parent
            elif line[2] == '/':
                cursor = root
            else:
                for child in cursor.children:
                    if child.name == line[2]:
                        cursor = child
                        break
        elif line[0] == '$' and line[1] == 'ls': # If a ls is found then ignore
            continue
        else: # if a file line is found
            cursor.children.append(Node(parent=cursor, name=line[1], size=line[0]))
            cursor.add_size(int(line[0]))
    
    return root
    

def solution(filename: str):

    with open(filename, 'r') as fh:
        ipt = [x.strip().split() for x in fh.readlines()]

    # Make the tree
    root = construct_tree(ipt)

    # For fun
    root.print_tree()

    # Part 1
    sum_ = root.sum_dirs_under_100000()
    print(f"Sum of dir with size < 100,000: {sum_}")

    # Part 2
    size_needed = root.size - 40_000_000
    smallest = root.smallest_above_threshold(threshold=root.size - 40_000_000)
    
    print(f"Size needed: {size_needed}")
    print(f"Smallest that will free enough space: {smallest}")


if __name__ == '__main__':
    test = 'test_input.txt'
    data = 'input.txt'
    solution(data)
