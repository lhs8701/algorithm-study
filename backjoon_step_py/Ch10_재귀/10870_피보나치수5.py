import sys

n = int(sys.stdin.readline().rstrip())


def fibo(n):
    if n < 2:
        return n
    return fibo(n - 2) + fibo(n - 1)


print(fibo(n))
