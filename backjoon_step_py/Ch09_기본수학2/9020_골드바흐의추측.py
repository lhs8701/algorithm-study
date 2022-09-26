import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    n = int(sys.stdin.readline().rstrip())

    num = [True] * (n + 1)
    num[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        for j in range(i * i, n + 1, i):
            num[j] = False

    ans1, ans2 = 0, 0
    start, end = n // 2, n // 2
    while True:
        while not num[start]:
            start -= 1
        while not num[end]:
            end += 1

        if start + end == n:
            ans1, ans2 = start, end
            break
        elif start + end > n:
            start -= 1
        else:
            end += 1

    print(ans1, ans2)
