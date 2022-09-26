import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)
