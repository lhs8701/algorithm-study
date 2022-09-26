import sys

numbers = [0] * 10
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
result = list(str(A * B * C))

for i in result:
    numbers[ord(i) - ord('0')] += 1

for i in numbers:
    print(i)
