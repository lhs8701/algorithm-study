import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)
