import math
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(N + 1)]
dp[0] = 0
square = []
i = 1
while i ** 2 <= 50000:
    square.append(i ** 2)
    i += 1

for i in range(1, N + 1):
    min_val = math.inf
    for j in square:
        if j > i:
            break
        min_val = min(min_val, dp[i - j])
    dp[i] = min_val + 1

print(dp[N])
