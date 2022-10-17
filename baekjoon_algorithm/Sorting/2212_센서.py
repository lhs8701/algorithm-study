import sys
import heapq

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensor = list(map(int, sys.stdin.readline().rstrip().split()))
sensor.sort()

arr = []
for i in range(1, len(sensor)):
    arr.append(sensor[i] - sensor[i - 1])

arr.sort(key=lambda x: -x)

ans = sensor[-1] - sensor[0]
cur = 1
while arr and cur < K:
    ans -= arr[0]
    del arr[0]
    cur += 1

print(ans)
