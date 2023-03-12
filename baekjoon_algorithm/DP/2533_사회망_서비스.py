import sys


def dfs(graph, v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, u, visited)
            dp[v][0] += min(dp[u])
            dp[v][1] += dp[u][0]


sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[1, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dfs(graph, 1, visited)
print(min(dp[1]))
