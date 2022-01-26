import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    deq = deque(sorted(arr))
    i = 0
    j = N - 1
    while deq:
        minFirst = deq.popleft()
        arr[i] = minFirst
        i += 1
        if deq:
            minSecond = deq.popleft()
            arr[j] = minSecond
            j -= 1
    maxVal = -1
    for i in range(1, N):
        if maxVal < abs(arr[i] - arr[i - 1]):
            maxVal = abs(arr[i] - arr[i - 1])
    print(maxVal)
