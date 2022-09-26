import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
for i in range(N):
    print(arr[i])
