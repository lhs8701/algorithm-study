import sys

start_limit = 0
max_val = -1


def recursion(idx, sum_val):
    global max_val, start_limit

    if idx == N + 1:
        max_val = max(max_val, sum_val)
        return
    temp = start_limit
    if start_limit <= idx and idx + arr[idx][0] <= N + 1:
        start_limit = idx + arr[idx][0]
        sum_val += arr[idx][1]
    recursion(idx + 1, sum_val)
    sum_val -= arr[idx][1]
    start_limit = temp
    recursion(idx + 1, sum_val)


N = int(sys.stdin.readline().rstrip())
arr = [0]
for i in range(N):
    T, P = map(int, sys.stdin.readline().rstrip().split())
    arr.append((T, P))

recursion(1, 0)
print(max_val)
