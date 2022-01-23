import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

print(sorted(arr,reverse=True))