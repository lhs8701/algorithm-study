N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs(cnt):
    if cnt == M:
        for i in res:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        res.append(arr[i])
        dfs(cnt + 1)
        res.pop()

dfs(0)