import sys

N = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
arr3 = [(arr2[i], i) for i in range(M)]
ans = [0] * M

arr1.sort()
arr3.sort()

i = 0
j = 0
while i < N and j < M:
    if arr1[i] == arr3[j][0]:
        ans[arr3[j][1]] = 1
        i += 1
        j += 1
    elif arr1[i] < arr3[j][0]:
        i += 1
    else:
        j += 1

for i in ans:
    print(i, end=" ")
