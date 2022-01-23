import sys
N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    data = sys.stdin.readline().rstrip().split()
    arr.append((data[0],int(data[1])))

arr.sort(key=lambda x:x[1])
for i in range(N):
    print(arr[i][0], end=" ")
