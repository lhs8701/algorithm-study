import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


def calc_measure(arr, value):
    sum = 0
    for i in range(len(arr)):
        sum += max(arr[i] - value, 0)
    return sum


def binary_search(arr, right, M):
    left = 0
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if calc_measure(arr, mid) >= M:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result


print(binary_search(arr, max(arr), M))

"""
4 6
19 15 10 17
"""
