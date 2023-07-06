import math
import sys


def relax(graph, dist, v):
    for w, u in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w


def bellman_ford(graph):
    dist = [math.inf for _ in range(N + 1)]
    dist[X] = 0
    for _ in range(N - 1):
        for i in range(1, N + 1):
            relax(graph, dist, i)
    return dist


N, M, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
graph_r = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((w, b))
    graph_r[b].append((w, a))

dist_to = bellman_ford(graph_r)
dist_from = bellman_ford(graph)

max_val = -1
for i in range(1, N + 1):
    max_val = max(max_val, dist_to[i] + dist_from[i])
print(max_val)
