import sys


def func(level, arr, start):
    if level >= M:
        for i in arr:
            print(i, end=' ')
        print()
        return
    for i in range(start, N):
        arr.append(numbers[i])
        func(level + 1, arr, i)
        arr.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
arr = []
func(0, arr, 0)
