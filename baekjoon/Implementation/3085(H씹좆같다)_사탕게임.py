import sys

def Swap(x,y):
    global arr
    i = x[0]
    j = x[1]
    k = y[0]
    l = y[1]
    temp = arr[i][j]
    arr[i][j] = arr[k][l]
    arr[k][l] = temp

def Count(i,j):
    global N
    global arr
    maxVal1 = 0
    maxVal2 = 0
    maxVal3 = 0
    maxVal4 = 0
    cnt = [1,1,1,1]
    maxVal = [0,0,0,0]
    for k in range(N - 1):
        if arr[i][k] == arr[i][k + 1]:
            cnt[0] += 1
        else:
            maxVal[0] = max(cnt[0], maxVal[0])
            cnt[0] = 1
    maxVal[0] = max(maxVal[0], cnt[0])

    for k in range(N - 1):
        if arr[i+1][k] == arr[i+1][k+1]:
            cnt[1] += 1
        else:
            maxVal[1] = max(cnt[1], maxVal[1])
            cnt[1] = 1
    maxVal[1] = max(maxVal[1], cnt[1])

    for k in range(N - 1):
        if arr[k][j] == arr[k + 1][j]:
            cnt[2] += 1
        else:
            maxVal[2] = max(cnt[2], maxVal[2])
            cnt[2] = 1
    maxVal[2] = max(maxVal[2], cnt[2])

    for k in range(N - 1):
        if arr[k][j+1] == arr[k + 1][j+1]:
            cnt[3] += 1
        else:
            maxVal[3] = max(cnt[3], maxVal[3])
            cnt[3] = 1
    maxVal[3] = max(maxVal[3], cnt[3])
    return max(maxVal)

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    temp.append(temp[len(temp)-1])
    arr.append(temp)
arr.append(arr[len(arr)-1])

maxVal = 0
for i in range(N):
    for j in range(N):
        Swap((i, j), (i, j + 1))
        maxVal = max(maxVal, Count(i, j))
        Swap((i, j), (i, j + 1))

        Swap((i, j), (i + 1, j))
        maxVal = max(maxVal, Count(i, j))
        Swap((i, j), (i + 1, j))

print(maxVal)
