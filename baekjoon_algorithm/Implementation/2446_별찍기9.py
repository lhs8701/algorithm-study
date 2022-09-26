import sys

N = int(sys.stdin.readline().rstrip())

for i in range(-(N - 1), N):
    n = abs(i)
    for j in range(N - 1 - n):
        print(' ', end="")
    for j in range(2 * n + 1):
        print('*', end="")
    print()
