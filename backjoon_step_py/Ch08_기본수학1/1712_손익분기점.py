import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
if C <= B:
    print(-1)
else:
    print(A // (C - B) + 1)
