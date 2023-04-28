import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    str = list(sys.stdin.readline().rstrip())
    print(str[0] + str[-1])

