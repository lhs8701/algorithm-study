import sys
from collections import deque


def bfs(x, y):
    global maze
    global N, M
    cnt = 0
    dir = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    queue = deque([(x, y)])
    maze[x][y] = 1
    while queue:
        v = queue.popleft()
        print(v)
        cnt += 1
        x = v[0]
        y = v[1]
        find = False
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[N][M]


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = []
maze.append([0] * (M + 2))
for i in range(N):
    temp = list(map(int, list(sys.stdin.readline().rstrip())))
    temp.insert(0, 0)
    temp.append(0)
    maze.append(temp)
maze.append([0] * (M + 2))

print(bfs(1, 1))
