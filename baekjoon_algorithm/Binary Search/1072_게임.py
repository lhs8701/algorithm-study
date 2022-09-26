import sys
import math

X, Y = map(int, sys.stdin.readline().rstrip().split())
Z = math.trunc(Y * 100 / X)


def binary_search(left, right):
    global X, Y, Z
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if math.trunc((Y + mid) * 100 / (X + mid)) != Z:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(binary_search(1, 1000000000))
