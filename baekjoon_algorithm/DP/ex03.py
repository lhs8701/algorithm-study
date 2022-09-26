import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [-1] * N
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(max(dp))
