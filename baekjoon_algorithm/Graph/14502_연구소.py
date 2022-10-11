import sys
import copy
from collections import deque


def bfs(graph, virus):
    global N, M, max_val
    queue = deque()
    visited = [[0 for j in range(M)] for i in range(N)]
    for v in virus:
        queue.append(v)
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    while queue:
        vx, vy = queue.popleft()
        for d in dir:
            if vx + d[0] < 0 or vx + d[0] >= N or vy + d[1] < 0 or vy + d[1] >= M:
                continue
            if graph[vx + d[0]][vy + d[1]] == 0 and visited[vx + d[0]][vy + d[1]] == 0:
                visited[vx + d[0]][vy + d[1]] = 1
                queue.append((vx + d[0], vy + d[1]))
    cnt_zero = 0
    cnt_visited = 0
    for i in range(N):
        cnt_zero += graph[i].count(0)
        cnt_visited += visited[i].count(1)
    max_val = max(max_val, cnt_zero - cnt_visited)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []
virus = []
max_val = -1
for i in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(arr)
    for j in range(len(arr)):
        if arr[j] == 2:
            virus.append((i, j))


def make_wall(cnt):
    if cnt == 3:
        bfs(graph, virus)
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


make_wall(0)
print(max_val)
