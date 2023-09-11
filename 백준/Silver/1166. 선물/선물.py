import math
import sys


def binarySearch(left, right):
    for i in range(100):
        mid = (left + right) / 2
        if (L // mid) * (W // mid) * (H // mid) >= N:
            left = mid
        else:
            right = mid
    return right


N, L, W, H = map(int, sys.stdin.readline().rstrip().split())
print(binarySearch(0, max(L, H, W)))
