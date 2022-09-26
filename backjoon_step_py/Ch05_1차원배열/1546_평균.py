import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0
M = max(arr)
for i in arr:
    sum += i / M * 100
print(sum / N)
