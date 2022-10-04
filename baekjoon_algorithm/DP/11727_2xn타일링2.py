import sys

n = int(sys.stdin.readline().rstrip())
dp = [1, 1]

for i in range(2, n + 1):
    dp.append((dp[i - 2] * 2 + dp[i - 1]) % 10007)
print(dp[n])
