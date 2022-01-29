import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    arr = []
    N = int(sys.stdin.readline().rstrip())
    for i in range(N):
        num = sys.stdin.readline().rstrip()
        arr.append(num)
    arr.sort()
    flag = True
    for i in range(1, N):
        n1 = arr[i]
        n2 = arr[i - 1]
        if len(n1) > len(n2):
            long_num = n1
            short_num = n2
        else:
            long_num = n2
            short_num = n1
        d = len(short_num)
        if short_num == long_num[0:d]:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
