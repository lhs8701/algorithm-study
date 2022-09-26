import sys

x = [0, 0, 0]
y = [0, 0, 0]
x[0], y[0] = map(int, sys.stdin.readline().rstrip().split())
x[1], y[1] = map(int, sys.stdin.readline().rstrip().split())
x[2], y[2] = map(int, sys.stdin.readline().rstrip().split())

if x[0] != x[1]:
    if x[0] == x[2]:
        print(x[1], end=' ')
    else:
        print(x[0], end=' ')
else:
    print(x[2], end=' ')

if y[0] != y[1]:
    if y[0] == y[2]:
        print(y[1], end=' ')
    else:
        print(y[0], end=' ')
else:
    print(y[2], end=' ')
