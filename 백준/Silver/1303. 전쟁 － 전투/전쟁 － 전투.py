from collections import deque

n, m = map(int, input().split())

war = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
power = [0 for _ in range(2)]

for i in range(m):
    war.append(list(input()))


def bfs(x, y, a):
    queue = deque()
    queue.append((x, y))
    war[x][y] = -1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if war[nx][ny] == a:
                war[nx][ny] = -1
                queue.append((nx, ny))
                cnt += 1
    return cnt * cnt


for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            power[0] += bfs(i, j, "W")
        if war[i][j] == "B":
            power[1] += bfs(i, j, "B")

print(" ".join(map(str, power)))