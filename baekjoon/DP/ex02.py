import sys

X = int(sys.stdin.readline().rstrip())
dp = [30001] * (X + 1)

dp[1] = 0
for i in range(1, X + 1):
    if i + 1 <= X:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if i * 2 <= X:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i * 3 <= X:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 5 <= X:
        dp[i * 5] = min(dp[i * 5], dp[i] + 1)

print(dp[X])
