import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    front = N % H
    back = N // H + 1
    if front == 0:
        front = H
        back -= 1
    print(front, end='')
    if back < 10:
        print('0', end='')
    print(back)
