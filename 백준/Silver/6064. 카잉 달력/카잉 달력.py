import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, x, y = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = 0
    b = 0
    while True:
        b = (b + abs(M - N)) % min(M, N)
        cnt += 1
        if b == 0:
            break
    last = cnt * max(M, N)
    m = x
    n = y
    while n <= last or m <= last:
        if n == m:
            break
        elif n < m:
            n += N
        else:
            m += M
    if n == m and n <= last:
        print(n)
    else:
        print(-1)
