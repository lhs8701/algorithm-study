import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                visited[u] = True
                queue.append(u)


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
parent = [1 for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
bfs(1)
for i in range(2, N + 1):
    print(parent[i])
