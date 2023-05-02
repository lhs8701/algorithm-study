import sys

sys.setrecursionlimit(50000)


def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    order.append(v)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
order = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
order.reverse()
for i in order:
    print(i, end=" ")
