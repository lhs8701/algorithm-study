import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    for i in S:
        print(R * i, end='')
    print('')
