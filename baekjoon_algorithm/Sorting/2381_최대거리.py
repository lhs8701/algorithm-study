import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    arr.append((x, y))

plus = [x + y for x, y in arr]
minus = [abs(x - y) for x, y in arr]
first = max(minus)
minus.remove(first)
second = max(minus)
print(max(abs(max(plus) - min(plus)), first + second))
