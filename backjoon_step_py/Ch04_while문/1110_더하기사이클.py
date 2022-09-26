import sys

N = int(sys.stdin.readline().rstrip())
r = N
cnt = 0


def func(num):
    front = num % 10
    back = (num % 10 + num // 10) % 10
    return front * 10 + back


while True:
    r = func(r)
    cnt += 1
    if r == N:
        break

print(cnt)
