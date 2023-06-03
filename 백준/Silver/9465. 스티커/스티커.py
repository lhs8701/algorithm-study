import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    matrix = []
    n = int(sys.stdin.readline().rstrip())
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
    dp = [[-1, -1, -1] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    dp[0][1] = matrix[1][0]
    ans = max(dp[0])
    if n > 1:
        dp[1][0] = dp[0][1] + matrix[0][1]
        dp[1][1] = dp[0][0] + matrix[1][1]
        ans = max(ans, max(dp[1]))
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1] + matrix[0][i], max(dp[i - 2]) + matrix[0][i])
        dp[i][1] = max(dp[i - 1][0] + matrix[1][i], max(dp[i - 2]) + matrix[1][i])
        ans = max(ans, max(dp[i]))
    print(ans)
    dp.clear()
    matrix.clear()
