import sys
from collections import deque


def bfs(start_row, start_col, zone_id):
    queue = deque([(start_row, start_col)])
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

    visited[start_row][start_col] = zone_id
    union_stat[zone_id][0] += 1
    union_stat[zone_id][1] += matrix[start_row][start_col]
    while queue:
        v_row, v_col = queue.popleft()
        for dir_row, dir_col in dir:
            u_row, u_col = v_row + dir_row, v_col + dir_col
            if (0 <= u_row < N) and (0 <= u_col < N) and visited[u_row][u_col] == 0 and L <= abs(
                    matrix[v_row][v_col] - matrix[u_row][u_col]) <= R:
                queue.append((u_row, u_col))
                visited[u_row][u_col] = zone_id
                union_stat[zone_id][0] += 1
                union_stat[zone_id][1] += matrix[u_row][u_col]


def relocate():
    temp = {}
    for k, v in union_stat.items():
        temp[k] = v[1] // v[0]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = temp[visited[i][j]]


N, L, R = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp)

day = -1
while True:
    union_stat = {}
    visited = [[0 for _ in range(N)] for _ in range(N)]
    day += 1
    zone_id = 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_stat[zone_id] = [0, 0]
                bfs(i, j, zone_id)
                zone_id += 1
    if zone_id == N * N + 1:
        break
    relocate()

print(day)
