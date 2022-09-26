import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(50) for j in range(i)]
print(sum(arr[A - 1:B]))
