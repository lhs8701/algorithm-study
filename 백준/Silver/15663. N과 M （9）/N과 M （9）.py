import sys


def back_tracking(level):
    if level == M:
        print(*arr)
        return
    dict = {i: False for i in set(numbers)}
    for i in range(N):
        if not used[i] and not dict[numbers[i]]:
            arr.append(numbers[i])
            used[i] = True
            back_tracking(level + 1)
            used[i] = False
            arr.pop()
            dict[numbers[i]] = True


N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()
used = [False for i in range(N)]
arr = []
back_tracking(0)
