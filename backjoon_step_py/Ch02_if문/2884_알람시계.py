import sys

H, M = map(int, sys.stdin.readline().rstrip().split())

if M < 45:
    if H == 0:
        print('{} {}'.format(23, 15 + M))
    else:
        print('{} {}'.format(H - 1, 15 + M))
else:
    print('{} {}'.format(H, M - 45))
