import sys


def binary_search(arr, find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == find:
            return True
        elif arr[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    return False

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
for i in find:
    if binary_search(arr, i):
        print('yes', end=' ')
    else:
        print('no', end=' ')

"""
5
8 3 7 9 2
3
5 7 9
"""