import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] * i for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M):
    c1, c2 = map(int, sys.stdin.readline().rstrip().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

cnt = 0


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(cnt - 1)
