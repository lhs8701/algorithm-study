import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for elem in arr:
    if elem < X:
        print(elem, end=' ')
