import sys
from collections import deque


def bfs(start_r, start_c):
    global N, M
    visited = [[False for _ in range(M)] for _ in range(N)]
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    ans = 0
    while queue:
        v_r, v_c = queue.popleft()
        for dr, dc in dir:
            u_r, u_c = v_r + dr, v_c + dc
            if 0 <= u_r < N and 0 <= u_c < M and not visited[u_r][u_c]:
                if matrix[u_r][u_c] == 'O':
                    queue.append((u_r, u_c))
                    visited[u_r][u_c] = True
                if matrix[u_r][u_c] == 'P':
                    queue.append((u_r, u_c))
                    visited[u_r][u_c] = True
                    ans += 1
    return ans if ans != 0 else 'TT'


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = []
start_r, start_c = 0, 0
for i in range(N):
    matrix.append((list(sys.stdin.readline().rstrip())))
    for j in range(M):
        if matrix[i][j] == 'I':
            start_r, start_c = i, j

print(bfs(start_r, start_c))
