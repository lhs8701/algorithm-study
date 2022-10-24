import sys

N = int(sys.stdin.readline().rstrip())

arr = [1 for i in range(10)]

for i in range(N - 1):
    temp = [0 for _ in range(10)]
    for j in range(10):
        temp[j] = sum(arr[j:])
    for j in range(10):
        arr[j] = temp[j]

print(sum(arr) % 10007)
