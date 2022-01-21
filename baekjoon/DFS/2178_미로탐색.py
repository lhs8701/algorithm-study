import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [[0] * (M + 2)]
for i in range(N):
    t = list(map(int, list(sys.stdin.readline().rstrip())))
    t.insert(0, 0)
    t.append(0)
    maze.append(t)
maze.append([0] * (M + 2))


def bfs(maze):
    queue = deque([(1, 1)])
    dir = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
    maze[1][1] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1


bfs(maze)
print(maze[N][M])
