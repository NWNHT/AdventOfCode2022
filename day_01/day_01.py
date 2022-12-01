
import time

def solution():
    print("\nSolution 1:")
    with open('input.txt', 'r') as fh:
        text = [x[:-1] for x in fh.readlines()]

    start = time.perf_counter()
    count = 0
    counts = []
    for line in text:
        if len(line):
            count += int(line)
        else:
            counts.append(count)
            count = 0
    else:
        counts.append(count)

    counts.sort(reverse=True)
    print(f"Time: {time.perf_counter() - start:0.8}")
    print(f"Highest: {counts[0]}")
    print(f"Sum of top 3: {sum(counts[:3])}")


def solution2():
    print("\nSolution 2:")
    with open('input.txt', 'r') as fh:
        text = fh.read()

    start = time.perf_counter()
    counts = sorted([eval(x.replace('\n', '+').strip('+')) for x in text.split('\n\n')], reverse=True)
    print(f"Time: {time.perf_counter() - start:0.8}")
    print(f"Highest: {counts[0]}")
    print(f"Sum of top 3: {sum(counts[:3])}")


if __name__ == '__main__':
    solution()

    solution2()
