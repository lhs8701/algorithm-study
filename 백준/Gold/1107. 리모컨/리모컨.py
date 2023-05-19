import sys

available = set([i for i in range(0, 10)])
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
remote = {str(x) for x in range(10)}

if M != 0:
    remote -= set(sys.stdin.readline().rstrip().split())

min_cnt = abs(100 - N)

for k in range(1000000):
    num = str(k)
    for i in range(len(num)):
        if num[i] not in remote:
            break
        if i == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - k) + len(num))

print(min_cnt)
