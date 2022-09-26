import sys

N = sys.stdin.readline().rstrip()
digit = len(N)
N = int(N)


def func(num):
    r = num
    sum = num
    while r > 0:
        sum += r % 10
        r //= 10
    return sum


ans = 0
for i in range(9 * digit, 0, -1):
    if func(N - i) == N:
        ans = N - i
        break
print(ans)
