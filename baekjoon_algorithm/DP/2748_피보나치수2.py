import sys

n = int(sys.stdin.readline().rstrip())
prev_first, prev_second = 1, 0
for i in range(2, n + 1):
    temp = prev_first + prev_second
    prev_second = prev_first
    prev_first = temp
print(prev_first)
