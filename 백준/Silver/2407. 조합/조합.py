import sys


def facto(num):
    if num == 0:
        return 1
    return num * facto(num - 1)


n, m = map(int, sys.stdin.readline().rstrip().split())
print(facto(n) // (facto(n - m) * facto(m)))
