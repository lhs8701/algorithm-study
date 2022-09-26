import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0


def hans(num):
    r = num
    d1 = r % 10
    d2 = r // 10 % 10
    diff = d2 - d1
    while r >= 10:
        d1 = r % 10
        d2 = r // 10 % 10
        if d2 - d1 != diff:
            return False
        r //= 10
    return True


for i in range(1, N + 1):
    if hans(i):
        cnt += 1
print(cnt)
