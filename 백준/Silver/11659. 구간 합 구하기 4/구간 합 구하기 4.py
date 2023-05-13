import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
commend = []
dp = [0 for _ in range(N)]
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    commend.append((a, b))

for a, b in commend:
    print(dp[b - 1] - dp[a - 1] + arr[a - 1])
