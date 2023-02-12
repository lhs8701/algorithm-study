import sys


def solve(arr, N):
    arr.sort()
    middle = N // 2 - 1 if N % 2 == 0 else (N + 1) // 2 - 1
    sum = 0

    for i in range(N - 1, middle, -1):
        sum += arr[i] * 2
    if N % 2 == 1:
        sum += arr[middle]
    return sum


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(solve(arr, N))
