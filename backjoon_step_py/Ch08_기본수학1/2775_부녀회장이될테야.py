import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    dp = [[0] * 15] * 15
    for i in range(15):
        dp[0][i] = i
        dp[i][1] = 1
    for i in range(1, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    print(dp[k][n])
