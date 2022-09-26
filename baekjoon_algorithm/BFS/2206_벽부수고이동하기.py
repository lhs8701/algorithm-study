import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maps = [[1] * (M + 2)]
for i in range(N):
    t = list(map(int, list(sys.stdin.readline().rstrip())))
    t.insert(0, 1)
    t.append(1)
    maps.append(t)
maps.append([1] * (M + 2))


def bfs(N, M):
    global maps
    visited = [[[sys.maxsize] * 2 for j in range(M + 2)] for i in range(N + 2)]
    dir = [(-1, 0), (+1, 0), (0, +1), (0, -1)]
    queue = deque([(1, 1, 0)])
    visited[1][1][0] = 1
    while queue:
        x, y, s = queue.popleft()
        if x == 0 or x == N + 1 or y == 0 or y == M + 1:
            continue
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if maps[nx][ny] == 0:
                if visited[nx][ny][s] == sys.maxsize:
                    visited[nx][ny][s] = visited[x][y][s] + 1
                    queue.append((nx, ny, s))
            else:
                if s == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    ans = min(visited[N][M])
    if ans == sys.maxsize:
        return -1
    else:
        return ans


print(bfs(N, M))
