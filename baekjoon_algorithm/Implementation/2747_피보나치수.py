import sys

n = int(sys.stdin.readline().rstrip())
first, second, answer = 0, 1, n
for i in range(n - 1):
    answer = first + second
    first = second
    second = answer

print(answer)
