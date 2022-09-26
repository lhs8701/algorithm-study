import sys

N = int(sys.stdin.readline().rstrip())


def facto(N):
    if N <= 1:
        return 1
    return N * facto(N - 1)


print(facto(N))
