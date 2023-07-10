import math
import sys


def relax(dist, v):
    flag = False
    for w, u in graph[v]:
        if dist[u] > dist[v] + w:
            dist[u] = dist[v] + w
            flag = True
    return flag


def bellman_ford():
    dist = [int(1e9) for _ in range(N + 1)]
    dist[1] = 0
    for i in range(N - 1):
        for v in range(1, N + 1):
            relax(dist, v)

    for v in range(1, N + 1):
        if relax(dist, v):
            return True

    return False


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph[S].append((T, E))
        graph[E].append((T, S))
    for i in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip().split())
        graph[S].append((-T, E))

    print('YES' if bellman_ford() else 'NO')
