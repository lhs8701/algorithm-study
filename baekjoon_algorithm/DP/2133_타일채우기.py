import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * 31
arr = [0] * 31
dp[0] = 1
arr[0] = 2
dp[2] = 3
for i in range(4, N + 1, 2):
    arr[i - 2] = arr[i - 4] + dp[i - 2] * 2
    dp[i] = dp[i - 2] * 3 + arr[i - 4]

print(dp[N])
