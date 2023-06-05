import sys
from collections import deque


def bfs(start_r, start_c):
    global n, m
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = 0
    while queue:
        v_r, v_c = queue.popleft()
        for dr, dc in dir:
            u_r, u_c = v_r + dr, v_c + dc
            if 0 <= u_r < n and 0 <= u_c < m and visited[u_r][u_c] == -1 and matrix[u_r][u_c] == 1:
                queue.append((u_r, u_c))
                visited[u_r][u_c] = visited[v_r][v_c] + 1
    return visited


n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
start_r, start_c = 0, 0
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if matrix[i][j] == 2:
            start_r, start_c = i, j

visited = bfs(start_r, start_c)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
