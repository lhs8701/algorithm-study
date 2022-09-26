import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{}: {} + {} = {}'.format(t + 1, A, B, A + B))
