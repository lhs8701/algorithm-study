import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
box = [[-1] * (M + 2)]
days = [[-1] * (M + 2) for i in range(N + 2)]
tomato = []
for i in range(N):
    t = list(map(int, list(sys.stdin.readline().rstrip().split())))
    for j in range(M):
        if t[j] == 1:
            tomato.append((i + 1, j + 1))
    t.insert(0, -1)
    t.append(-1)
    box.append(t)
box.append([-1] * (M + 2))


def bfs(tomato):
    global box, days
    dir = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    queue = deque([])
    for i in tomato:
        queue.append(i)
        days[i[0]][i[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if box[nx][ny] == 0 and days[nx][ny] == -1:
                days[nx][ny] = days[x][y] + 1
                queue.append((nx, ny))


bfs(tomato)
flag = True
ans = -1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if box[i][j] == 0 and days[i][j] == -1:
            ans = -1
            flag = False
            break
        ans = max(ans, days[i][j])
    if not flag:
        break
print(ans)
