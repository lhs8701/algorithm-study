import sys

N = int(sys.stdin.readline().rstrip())
matrix = []
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
RIGHT = 0
DOWN = 1
DIAG = 2
dp[0][1][RIGHT] = 1

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(N):
        if 0 <= j - 1 and matrix[i][j] != 1:
            dp[i][j][RIGHT] = max(dp[i][j][RIGHT], dp[i][j - 1][RIGHT] + dp[i][j - 1][DIAG])
        if 0 <= i - 1 and matrix[i][j] != 1:
            dp[i][j][DOWN] = max(dp[i][j][DOWN], dp[i - 1][j][DOWN] + dp[i - 1][j][DIAG])
        if 0 <= i - 1 and 0 <= j - 1 and matrix[i][j] != 1 and matrix[i - 1][j] != 1 and matrix[i][j - 1] != 1:
            dp[i][j][DIAG] = max(dp[i][j][DIAG], sum(dp[i - 1][j - 1]))

print(sum(dp[N - 1][N - 1]))
