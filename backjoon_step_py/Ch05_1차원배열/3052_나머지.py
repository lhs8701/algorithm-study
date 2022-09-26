import sys

remainder = [0] * 42
for i in range(10):
    num = int(sys.stdin.readline().rstrip())
    remainder[num % 42] += 1

cnt = 0
for i in remainder:
    if i != 0:
        cnt += 1
print(cnt)
