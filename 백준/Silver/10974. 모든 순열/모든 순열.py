import sys


def func(level):
    if level >= N:
        for i in queue:
            print(i, end=' ')
        print()
        return
    for number in range(1, N + 1):
        if not used[number]:
            queue.append(number)
            used[number] = True
            func(level + 1)
            queue.pop()
            used[number] = False


N = int(sys.stdin.readline().rstrip())
used = [False for _ in range(N + 1)]
queue = []
func(0)
