import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
stack = deque([])
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

d = max(dp)
print(d)

for i in range(N - 1, -1, -1):
    if d == 0:
        break
    if dp[i] == d:
        stack.appendleft(arr[i])
        d -= 1

for i in stack:
    print(i, end=' ')
