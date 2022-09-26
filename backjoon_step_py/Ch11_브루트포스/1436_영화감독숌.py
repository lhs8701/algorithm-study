import sys


def func(num):
    r = num
    cnt = 0
    while r != 0:
        if r % 10 == 6:
            cnt += 1
        else:
            break
        r //= 10
    return cnt


N = int(sys.stdin.readline().rstrip())

n = 0
order = 1
while True:
    c = n * 1000 + 666
    cont = func(n)
    d = 10 ** cont
    if cont == 0:
        cur = c
    else:
        cur = c // d * d
    if N < order + d:
        print(cur + N - order)
        break
    n += 1
    order += d
