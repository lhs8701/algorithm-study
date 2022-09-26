import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
num = [True] * 1001
num[1] = False
for i in range(2, 1001):
    if i * i > 1000:
        break
    for j in range(i * i, 1001, i):
        num[j] = False

cnt = 0
for i in range(N):
    if num[arr[i]]:
        cnt += 1
print(cnt)
