import math
import sys


def upper_bound(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, K = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    diff = [math.inf for _ in range(n)]
    arr.sort()
    for i in range(n - 1):
        idx = upper_bound(i + 1, n - 1, K - arr[i])
        if idx != i + 1 and abs(K - (arr[i] + arr[idx])) > abs(K - (arr[i] + arr[idx - 1])):
            idx -= 1
        diff[i] = abs(K - (arr[i] + arr[idx]))
    min_val = min(diff)
    print(diff.count(min_val))

