import sys

C = int(sys.stdin.readline().rstrip())
for c in range(C):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    N = arr[0]
    del arr[0]
    sum_val = sum(arr)
    average = sum_val / N
    cnt = 0
    for i in arr:
        if i > average:
            cnt += 1
    print('%.3f%%' % (cnt * 100 / N))
