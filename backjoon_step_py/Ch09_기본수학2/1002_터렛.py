import sys
import math

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    d = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    if d == 0 and r1 == r2:
        print(-1)
    elif d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    elif d == abs(r1 - r2):
        print(1)
    elif d < abs(r1 - r2):
        print(0)
    else:
        print(2)
