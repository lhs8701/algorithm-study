import sys


def floydWarshall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    return


n, m, r = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for i in range(r):
    a, b, l = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = l
    graph[b][a] = l

floydWarshall()
answer = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            answer[i] += items[j - 1]

print(max(answer))
