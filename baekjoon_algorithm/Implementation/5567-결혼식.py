import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
arr = [[i] for i in range(0,n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(len(arr[1])):
    f = arr[1][i]
    for j in range(len(arr[f])):
        ff = arr[f][j]
        if ff not in arr[1]:
            arr[1].append(ff)

print(len(arr[1])-1)
