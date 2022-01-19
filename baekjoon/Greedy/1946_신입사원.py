import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = []
    N = int(sys.stdin.readline().rstrip())
    for j in range(N):
        s1, s2 = map(int, sys.stdin.readline().rstrip().split())
        arr.append((s1,s2))
    arr.sort(key = lambda x:x[0])
    minVal = arr[0][1]
    cnt = 0
    for j in range(1,N):
        if minVal<arr[j][1]:
            cnt+=1
        minVal = min(minVal,arr[j][1])
    print(N-cnt)