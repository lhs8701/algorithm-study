import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
num = [True] * 1000001
num[1] = False
for i in range(2, 1000001):
    if i * i > 1000000:
        break
    for j in range(i * i, 1000001, i):
        num[j] = False

cnt = 0
for i in range(M, N + 1):
    if num[i]:
        print(i)
