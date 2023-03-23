import sys


def calculate(num):
    return (num + 1) * (n - num + 1)


def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        val = calculate(mid)
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


n, k = map(int, sys.stdin.readline().rstrip().split())
if binary_search(0, n//2, k):
    print('YES')
else:
    print('NO')
