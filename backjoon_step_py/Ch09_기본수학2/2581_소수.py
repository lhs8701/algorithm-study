import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

num = [True] * 10001
num[1] = False
for i in range(2, 10001):
    if i * i > 10000:
        break
    for j in range(i * i, 10001, i):
        num[j] = False

flag = True
sum = 0
min = 0
for i in range(M, N + 1):
    if num[i]:
        if flag:
            min = i
            flag = False
        sum += i

print(-1 if flag else '{} {}'.format(sum, min))
