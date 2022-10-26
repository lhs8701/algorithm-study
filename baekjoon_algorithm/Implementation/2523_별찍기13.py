import sys

N = int(sys.stdin.readline().rstrip())
for i in range(1, 2 * N):
    n = N - abs(i - N)
    for j in range(n):
        print("*", end='')
    print()
