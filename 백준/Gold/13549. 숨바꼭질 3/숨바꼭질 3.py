import sys
from collections import deque


def bfs(start):
    visited = [-1 for _ in range(100001)]
    visited[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v]
        if v * 2 <= 100000 and visited[v * 2] == -1:
            visited[v * 2] = visited[v]
            queue.append(v * 2)
        if v - 1 >= 0 and visited[v - 1] == -1:
            visited[v - 1] = visited[v] + 1
            queue.append(v - 1)
        if v + 1 <= 100000 and visited[v + 1] == -1:
            visited[v + 1] = visited[v] + 1
            queue.append(v + 1)
        


N, K = map(int, sys.stdin.readline().rstrip().split())
print(bfs(N))
