import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for i in range(N + 1)]
visited = []
min_val = sys.maxsize
max_val = 0

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    min_val = min(min_val, C)
    max_val = max(max_val, C)

start, end = map(int, sys.stdin.readline().rstrip().split())


def bfs(graph, value):
    global start, end, visited
    visited = [False] * (N + 1)
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == end:
            return True
        for bridge in graph[v]:
            if not visited[bridge[0]] and bridge[1] >= value:
                visited[bridge[0]] = True
                queue.append(bridge[0])

    return False


def binary_search(graph, left, right):
    global start, end, visited
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if bfs(graph, mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


print(binary_search(graph, min_val, max_val))