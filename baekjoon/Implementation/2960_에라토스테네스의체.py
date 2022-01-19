import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

arr = [i for i in range(N+1)]

cnt = 0
ans = 0
found = False
n = 0
while True:
    for i in range(2,len(arr)):
        if arr[i] != -1:
            n = arr[i]
            break
    for i in range(2,len(arr)):
        if arr[i] % n == 0:
            cnt+=1
            if cnt == K:
                ans=arr[i]
                found=True
                break
            arr[i] = -1
    if found:
        break

print(ans)


