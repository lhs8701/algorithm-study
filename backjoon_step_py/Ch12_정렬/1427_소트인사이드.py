import sys

N = list(map(int, sys.stdin.readline().rstrip()))
N.sort(key=lambda x: -x)
for i in N:
    print(i, end='')
