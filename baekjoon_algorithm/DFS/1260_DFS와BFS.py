import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] * i for i in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    graph[i].sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    print(v, end=' ')
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)


visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)
