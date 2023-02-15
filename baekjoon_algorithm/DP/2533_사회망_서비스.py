import math
import sys
import heapq


def solve(graph, N):
    global early_adopter
    vertex = set([i for i in range(1, N + 1)])
    non_leaf = set(parent)
    leaf = vertex.difference(non_leaf)
    early_adopter = [0 for _ in range(N + 1)]
    dp = [[0, 1] for _ in range(0, N + 1)]
    heap = list(set(parent[i] * -1 for i in leaf))
    while True:
        cur = heapq.heappop(heap) * -1
        if cur == -1:
            break
        sum_0 = 0
        sum_1 = 0
        for v in graph[cur]:
            if v != parent[cur]:
                sum_0 += dp[v][1]
                sum_1 += min(dp[v])
        dp[cur][0] = sum_0
        dp[cur][1] = sum_1 + 1
        heapq.heappush(heap, parent[cur] * -1)
    return min(dp[1])


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    parent[max(u, v)] = min(u, v)
    graph[u].append(v)
    graph[v].append(u)
print(solve(graph, N))