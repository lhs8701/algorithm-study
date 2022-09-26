import sys

sys.setrecursionlimit(100000)
T = int(sys.stdin.readline().rstrip())

dir = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def dfs(x, y):
    global farm
    global dir
    farm[x][y] = 0
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if farm[nx][ny] == 1:
            dfs(nx, ny)


for t in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    farm = [[0] * (N + 2) for i in range(M + 2)]
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        farm[X + 1][Y + 1] = 1

    cnt = 0
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if farm[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
