import sys


def move_one(r, c, move_d, move_s):
    global N
    dir = [(0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1)]
    return (r + dir[move_d - 1][0] * move_s) % N, (c + dir[move_d - 1][1] * move_s) % N


def move_cloud(cloud, move_d, move_s):
    for i in range(len(cloud)):
        cloud[i] = move_one(cloud[i][0], cloud[i][1], move_d, move_s)


def rain(matrix, cloud):
    for r_cloud, c_cloud in cloud:
        matrix[r_cloud][c_cloud] += 1


def count_of_bucket(matrix, r, c):
    global N
    cnt = 0
    dir = [(-1, -1), (-1, +1), (+1, +1), (+1, -1)]
    for r_dir, c_dir in dir:
        r_diag, c_diag = r + r_dir, c + c_dir
        if 0 <= r_diag < N and 0 <= c_diag < N and matrix[r_diag][c_diag] > 0:
            cnt += 1
    return cnt


def water_copy(matrix, cloud):
    for r, c in cloud:
        matrix[r][c] += count_of_bucket(matrix, r, c)


def update_cloud(matrix, cloud):
    global N
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2:
                temp[i][j] = -2

    for r, c in cloud:
        temp[r][c] = 0

    cloud.clear()
    for i in range(N):
        for j in range(N):
            if temp[i][j] == -2:
                cloud.append([i, j])

    for i in range(N):
        for j in range(N):
            matrix[i][j] += temp[i][j]



N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = []
move = []
cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp)

for i in range(M):
    d, s = map(int, sys.stdin.readline().rstrip().split())
    move.append((d, s))

for d, s in move:  # M
    move_cloud(cloud, d, s)  # N^2
    rain(matrix, cloud)  # N^2
    water_copy(matrix, cloud)  # N^2
    update_cloud(matrix, cloud)  # N^2

ans = 0
for i in range(N):
    ans += sum(matrix[i])

print(ans)
