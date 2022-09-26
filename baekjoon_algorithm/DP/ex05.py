import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
digit = []
for i in range(N):
    digit.append(int(sys.stdin.readline().rstrip()))

dp = [10001] * (M + 1)
dp[0] = 0
for i in range(0, M + 1):
    if dp[i] != 10001:
        for j in range(N):
            if i + digit[j] <= M:
                dp[i + digit[j]] = min(dp[i + digit[j]], dp[i] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
