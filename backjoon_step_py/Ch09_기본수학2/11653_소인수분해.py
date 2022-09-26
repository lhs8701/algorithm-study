import sys

N = int(sys.stdin.readline().rstrip())
r = N
i = 2
while r != 1:
    if r % i == 0:
        print(i)
        r //= i
        i = 2
    else:
        i += 1
