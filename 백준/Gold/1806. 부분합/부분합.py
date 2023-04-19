import math
import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = 0
sum_val = arr[0]
cur_len = 1
min_len = math.inf

while left <= right:
    if sum_val >= S:
        min_len = min(cur_len, min_len)
    if sum_val < S:
        if right + 1 < N:
            right += 1
        else:
            break
        sum_val += arr[right]
        cur_len += 1
    else:
        sum_val -= arr[left]
        left += 1
        cur_len -= 1

print(min_len if min_len != math.inf else 0)
