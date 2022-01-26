import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

remain = L - 1
cnt = 1
for i in range(1, N):
    if remain >= arr[i] - arr[i - 1]:
        remain -= arr[i] - arr[i - 1]
    else:
        remain = L - 1
        cnt += 1
print(cnt)
