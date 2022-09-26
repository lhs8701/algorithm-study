import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
maps = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    maps.append(temp)


def TurnLeft(d):
    if d == 3:
        return 0
    else:
        return d + 1


def Dfs(r, c, d):
    global maps
    cnt = 0
    dir = [(-1, 0), (0, -1), (+1, 0), (0, +1)]
    visited = [[False] * M for i in range(N)]
    while True:
        flag = False
        if not visited[r][c]:
            visited[r][c] = True
            cnt += 1
        for i in range(4):
            d = TurnLeft(d)
            nx = r + dir[d][0]
            ny = c + dir[d][1]
            if maps[nx][ny] == 0 and not visited[nx][ny]:
                r = nx
                c = ny
                flag = True
                break
        if flag:
            continue
        if maps[r - dir[d][0]][c - dir[d][1]] == 1:
            break
        else:
            r -= dir[d][0]
            c -= dir[d][1]
    return cnt


if d == 1:
    d = 3
elif d == 3:
    d = 1
print(Dfs(r, c, d))
