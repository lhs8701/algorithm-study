import math
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(N + 1)]
arr = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    func_three = math.inf
    func_two = math.inf
    if i % 3 == 0:
        func_three = dp[i // 3]
    if i % 2 == 0:
        func_two = dp[i // 2]
    func_one = dp[i - 1]
    if func_one < func_two:
        if func_one < func_three:
            dp[i] = func_one + 1
            arr[i] = i - 1
        else:
            dp[i] = func_three + 1
            arr[i] = i // 3
    else:
        if func_two < func_three:
            dp[i] = func_two + 1
            arr[i] = i // 2
        else:
            dp[i] = func_three + 1
            arr[i] = i // 3

arr.append(N)
print(dp[N])
r = N
while r != 0:
    print(r, end=' ')
    r = arr[r]
