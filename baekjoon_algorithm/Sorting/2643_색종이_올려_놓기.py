import sys

N = int(sys.stdin.readline().rstrip())
temp = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    temp.append((min(a, b), max(a, b)))

temp.sort()
arr = [elem[1] for elem in temp]
cnt = [1 for i in range(N)]
for i in range(1, N):
    max_val = 0
    for j in range(i):
        if arr[j] <= arr[i]:
            max_val = max(max_val, cnt[j])
    cnt[i] = max_val + 1
print(max(cnt))

# ----- upper_bound 이용 ----- #

import sys


def upper_bound(lis, key, right):
    left = 0
    while left < right:
        mid = (left + right) // 2
        if lis[mid] <= key:
            left = mid + 1
        else:
            right = mid
    return left


N = int(sys.stdin.readline().rstrip())
temp = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    temp.append((min(a, b), max(a, b)))
temp.sort()
arr = [elem[1] for elem in temp]
lis = [arr[0]]
for i in range(1, N):
    idx = upper_bound(lis, arr[i], len(lis))
    if idx == len(lis):
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]

print(len(lis))
