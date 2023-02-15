import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.append(0)
arr.sort()
zero_idx = arr.index(0)

sum = 0
for l in range(0, zero_idx, M):
    sum += abs(arr[l]) * 2

for r in range(N, zero_idx, -M):
    sum += abs(arr[r]) * 2

big_number = max(abs(arr[0]), abs(arr[-1]))
print(sum - big_number)
