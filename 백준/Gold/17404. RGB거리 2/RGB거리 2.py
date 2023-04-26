import math
import sys

N = int(sys.stdin.readline().rstrip())
house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[[math.inf for _ in range(3)] for _ in range(3)] for _ in range(N)]
arr = [[[math.inf for _ in range(3)] for _ in range(3)] for _ in range(N)]

dp[0][0] = [house[0][0], math.inf, math.inf]
dp[0][1] = [math.inf, house[0][1], math.inf]
dp[0][2] = [math.inf, math.inf, house[0][2]]

for i in range(1, N):
    for j in range(3):
        dp[i][j][0] = min(dp[i - 1][j][1], dp[i - 1][j][2]) + house[i][0]
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + house[i][1]
        dp[i][j][2] = min(dp[i - 1][j][0], dp[i - 1][j][1]) + house[i][2]

print(min(min(dp[N - 1][0][1:3]), min(dp[N - 1][1][0:3:2]), min(dp[N - 1][2][0:2])))
