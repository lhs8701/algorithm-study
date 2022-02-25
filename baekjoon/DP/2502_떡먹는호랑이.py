import sys

D, K = map(int, sys.stdin.readline().rstrip().split())

dp_x = [0] * (D + 1)
dp_y = [0] * (D + 1)

dp_x[1], dp_y[1] = 1, 0
dp_x[2], dp_y[2] = 0, 1

for i in range(3, D + 1):
    dp_x[i] = dp_x[i - 1] + dp_x[i - 2]
    dp_y[i] = dp_y[i - 1] + dp_y[i - 2]

for i in range(1, K + 1):
    r = K - dp_x[D] * i
    if r % dp_y[D] == 0:
        print(i)
        print(r // dp_y[D])
        break

