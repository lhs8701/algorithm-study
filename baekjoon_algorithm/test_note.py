import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    temp = a % 10
    ans = temp
    for i in range(b - 1):
        ans = (ans * temp) % 10
    print(10 if ans == 0 else ans)
