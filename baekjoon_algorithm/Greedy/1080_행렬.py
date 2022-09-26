import sys


def trans_mat(mat, x, y):
    for i in range(3):
        for j in range(3):
            mat[x + i][y + j] = 1 if mat[x + i][y + j] == 0 else 0


N, M = map(int, sys.stdin.readline().rstrip().split())
mat_a, mat_b = [], []
cnt = 0

for i in range(N):
    mat_a.append(list(map(int, sys.stdin.readline().rstrip())))
for i in range(N):
    mat_b.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(N - 2):
    for j in range(M - 2):
        if mat_a[i][j] != mat_b[i][j]:
            trans_mat(mat_a, i, j)
            cnt += 1

if mat_a == mat_b:
    print(cnt)
else:
    print(-1)
