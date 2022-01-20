import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(N):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))


def dfs(x, y):
    global arr
    if x < 0 or y > M or x > N or y < 0:
        return

    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)


cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
