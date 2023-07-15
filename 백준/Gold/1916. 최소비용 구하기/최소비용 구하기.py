import math
import sys


def relax(dist, v):
    for w, u in graph[v]:
        if dist[u] > dist[v] + w:
            dist[u] = dist[v] + w


def get_min(dist, visited):
    min_idx = 0
    for i in range(1, N + 1):
        if not visited[i] and dist[min_idx] > dist[i]:
            min_idx = i
    return min_idx


def dijkstra(start, end):
    dist = [math.inf for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    dist[start] = 0
    for _ in range(N):
        v = get_min(dist, visited)
        visited[v] = True
        relax(dist, v)

    return dist[end]


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(N + 1)]
for _ in range(M):
    S, E, W = map(int, sys.stdin.readline().rstrip().split())
    graph[S].append((W, E))
start, end = map(int, sys.stdin.readline().rstrip().split())
print(dijkstra(start, end))
