import sys
import math
import heapq


def lower_bound(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid + 1
    return right


def upper_bound(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid + 1
    return right


N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

print(round(sum(arr) / N))
arr.sort()

print(arr[len(arr) // 2])

idx = 0
max = -1
max_numbers = []
while idx < N:
    up = upper_bound(arr, arr[idx])
    lw = lower_bound(arr, arr[idx])
    cnt = up - lw
    if max < cnt:
        max = cnt
        max_numbers = []
        heapq.heappush(max_numbers, arr[idx])
    elif max == cnt:
        heapq.heappush(max_numbers, arr[idx])
    idx = up

ans = heapq.heappop(max_numbers)
if max_numbers:
    ans = heapq.heappop(max_numbers)
print(ans)

print(arr[-1] - arr[0])
