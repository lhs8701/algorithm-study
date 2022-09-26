import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())
H = A
M = B + C
if M >= 60:
    H += M // 60
print('{} {}'.format(H % 24, M % 60))
