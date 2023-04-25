import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
question = []
dp = [[False for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    S, E = map(int, sys.stdin.readline().rstrip().split())
    question.append((S, E))

arr.insert(0, -1)
for i in range(1, N + 1):
    dp[i][i] = True

for i in range(1, N):
    for j in range(1, i + 1):
        for k in range(j, N, i):
            if k + i <= N:
                success = True
                if k + 1 <= k + i - 1:
                    success = dp[k + 1][k + i - 1]
                dp[k][k + i] = success and arr[k] == arr[k + i]

for i in question:
    print(1 if dp[i[0]][i[1]] else 0)
