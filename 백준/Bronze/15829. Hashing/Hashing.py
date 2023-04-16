import sys

L = int(sys.stdin.readline().rstrip())
str = sys.stdin.readline().rstrip()
sum = 0
for i in range(L):
    idx = ord(str[i]) - 96
    sum += idx * (31 ** i) % 1234567891

print(sum)