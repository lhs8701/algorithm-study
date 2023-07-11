import sys


def comb(storage, level, prev):
    if level == M:
        print(*storage)
        return
    for i in range(prev, length):
        storage.append(numbers[i])
        comb(storage, level + 1, i)
        storage.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = list(set(map(int, sys.stdin.readline().rstrip().split())))
numbers.sort()
length = len(numbers)
comb([], 0, 0)
