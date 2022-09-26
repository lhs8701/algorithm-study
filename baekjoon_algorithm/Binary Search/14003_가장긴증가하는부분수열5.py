import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
lis = [arr[0]]
len_ = [0] * N
stack = deque([])


def lower_bound(arr, elem):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= elem:
            right = mid
        else:
            left = mid + 1
    return left


for i in range(1, N):
    idx = lower_bound(lis, arr[i])
    if idx == len(lis):
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]
    len_[i] = idx

d = len(lis) - 1
print(d + 1)

for i in range(N - 1, -1, -1):
    if d == -1:
        break
    if len_[i] == d:
        stack.appendleft(arr[i])
        d -= 1

for i in stack:
    print(i, end=' ')
