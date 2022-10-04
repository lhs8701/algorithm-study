import sys

N = int(sys.stdin.readline().rstrip())
dp = [[0, 0], [0, 1]]

for i in range(2, N + 1):
    zero = dp[i-1][0] + dp[i-1][1]
    one = dp[i-1][0]
    dp.append([zero, one])

print(sum(dp[N]))
