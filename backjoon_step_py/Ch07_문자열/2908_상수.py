import sys

A, B = map(list, sys.stdin.readline().rstrip().split())
A.reverse()
B.reverse()
A = ''.join(A)
B = ''.join(B)
if A > B:
    print(A)
else:
    print(B)
