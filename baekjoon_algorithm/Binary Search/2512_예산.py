import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())


def binary_search(arr, right, M):
    left = 0
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        sum = 0
        for i in arr:
            sum += min(i, mid)
        if sum > M:
            right = mid - 1
        else:
            left = mid + 1
            ans = min(max(arr), mid)
    return ans


print(binary_search(arr, max(arr), M))
