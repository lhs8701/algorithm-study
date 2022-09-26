import sys

N = int(sys.stdin.readline().rstrip())
arr = [[' ' for i in range(N)] for j in range(N)]


def func(startx, starty, length):
    if length == 1:
        arr[startx][starty] = '*'
        return
    n = length // 3
    for i in range(9):
        if i == 4:
            continue
        a, b = startx + i // 3 * n, starty + i % 3 * n
        func(a, b, n)


func(0, 0, N)
for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()
