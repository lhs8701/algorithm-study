import sys

sys.setrecursionlimit(10000)
N = int(sys.stdin.readline().rstrip())
maps = [['X'] * (N + 2)]
dir = [(-1, 0), (0, -1), (+1, 0), (0, +1)]
cnt = 0
cnt2 = 0
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    temp.insert(0, 'X')
    temp.append('X')
    maps.append(temp)
maps.append(['X'] * (N + 2))


def Dfs(x, y, visited):
    global maps, dir, mark
    visited[x][y] = True
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if not visited[nx][ny] and maps[x][y] == maps[nx][ny]:
            Dfs(nx, ny, visited)
    if maps[x][y] == 'G':
        maps[x][y] = 'R'
    return


visited = [[False] * (N + 2) for i in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if not visited[i][j]:
            Dfs(i, j, visited)
            cnt += 1

visited = [[False] * (N + 2) for i in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if not visited[i][j]:
            Dfs(i, j, visited)
            cnt2 += 1
print(cnt, cnt2)
