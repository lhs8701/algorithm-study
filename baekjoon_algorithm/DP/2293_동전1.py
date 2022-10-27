

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(coins[i], k + 1):
        dp[j] += dp[j - coins[i]]

print(dp[k])
