import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
not_heard = set()
not_saw = set()
dict = {}
arr = []
for i in range(N):
    not_heard.add(sys.stdin.readline().rstrip())

for j in range(N):
    not_saw.add(sys.stdin.readline().rstrip())

arr = list(not_saw & not_heard)

arr.sort()
print(len(arr))
for i in arr:
    print(i)
