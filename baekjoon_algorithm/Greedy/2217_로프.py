
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
max = 0
for i in range(N):
    if max < (N-i)*arr[i]:
        max = (N-i)*arr[i]

print(max)