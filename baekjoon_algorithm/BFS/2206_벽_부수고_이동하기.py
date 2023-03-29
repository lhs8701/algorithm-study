import math
import sys
from collections import deque


def bfs(start_row, start_col):
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    queue = deque([(start_row, start_col, False)])
    visited[start_row][start_col][0] = 1
    while queue:
        v_row, v_col, used = queue.popleft()
        for dir_row, dir_col in dir:
            u_row, u_col = v_row + dir_row, v_col + dir_col
            if 0 <= u_row < N and 0 <= u_col < M:
                if matrix[u_row][u_col] == 0:
                    if visited[u_row][u_col][used] == math.inf:
                        queue.append((u_row, u_col, used))
                        visited[u_row][u_col][used] = visited[v_row][v_col][used] + 1
                else:
                    if not used:
                        queue.append((u_row, u_col, True))
                        visited[u_row][u_col][1] = visited[v_row][v_col][0] + 1


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = []
NONE = N * M + 1
visited = [[[math.inf, math.inf] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

bfs(0, 0)
ans = min(visited[N - 1][M - 1])
print(-1 if ans == math.inf else ans)
