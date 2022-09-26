import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
sum = 0

for i in range(3):
    print(A * (B % 10))
    sum += A * (B % 10) * (10 ** i)
    B //= 10
print(sum)
