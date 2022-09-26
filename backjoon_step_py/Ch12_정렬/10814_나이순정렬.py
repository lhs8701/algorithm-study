import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x: x[0])
for i in arr:
    print(i[0], i[1])
