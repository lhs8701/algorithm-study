import sys

arr = list(map(int, sys.stdin.readline().rstrip().split()))
sum = 0
for i in range(5):
    sum += arr[i] ** 2

print(sum % 10)
