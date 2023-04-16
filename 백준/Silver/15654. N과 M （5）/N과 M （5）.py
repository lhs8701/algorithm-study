import sys


def func(level, arr):
    if level >= M:
        for i in arr:
            print(i, end=' ')
        print()
        return
    for i in range(N):
        if numbers[i] not in arr:
            arr.append(numbers[i])
            func(level + 1, arr)
            arr.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
arr = []
func(0, arr)
