# import sys
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# coins = []
# dp = [[0 for j in range(n)] for i in range(k + 1)]
#
# for i in range(n):
#     coins.append(int(sys.stdin.readline().rstrip()))
#
# for i in range(n):
#     dp[coins[i]][i] = 1
#
# for i in range(k + 1):
#     for j in range(n):
#         if i - coins[j] >= 1:
#             sum_ = 0
#             for m in range(j, n):
#                 sum_ += dp[i - coins[j]][m]
#             dp[i][j] = sum_
#
# print(sum(dp[k]))

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
