import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    num = [True] * (2 * n + 1)
    num[1] = False
    for i in range(2, 2 * n + 1):
        if i * i > 2 * n:
            break
        for j in range(i * i, 2 * n + 1, i):
            num[j] = False

    sum = 0
    for i in range(n + 1, 2 * n + 1):
        if num[i]:
            sum += 1
    print(sum)
