import sys

N = int(sys.stdin.readline().rstrip())
maps = [[0] * (N + 2)]
complexs = []
dir = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
cnt = 0
for i in range(N):
    temp = list(map(int, list(sys.stdin.readline().rstrip())))
    temp.insert(0, 0)
    temp.append(0)
    maps.append(temp)
maps.append([0] * (N + 2))


def dfs(i, j):
    global maps
    global num
    maps[i][j] = 0
    num += 1
    for k in range(4):
        nx = i + dir[k][0]
        ny = j + dir[k][1]
        if maps[nx][ny] == 1:
            dfs(nx, ny)


for i in range(1, N + 1):
    for j in range(1, N + 1):
        num = 0
        if maps[i][j] == 1:
            cnt += 1
            dfs(i, j)
            complexs.append(num)

print(cnt)
complexs.sort()
for i in complexs:
    print(i)
