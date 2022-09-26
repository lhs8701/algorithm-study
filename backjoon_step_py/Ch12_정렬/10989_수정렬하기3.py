import sys

N = int(sys.stdin.readline().rstrip())
num = [0] * 10001

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    num[n] += 1

for i in range(10001):
    for j in range(num[i]):
        print(i)
