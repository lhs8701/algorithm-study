import sys
from collections import deque


def bfs(v, visited):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if visited[u] == -1:
                visited[u] = visited[v] + 1
                queue.append(u)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
level = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N + 1):
    visited = [-1 for _ in range(N + 1)]
    visited[i] = 0
    bfs(i, visited)
    level[i] = sum(visited[1:])

min_idx = 1
for i in range(2, N + 1):
    if level[i] < level[min_idx]:
        min_idx = i

print(min_idx)
