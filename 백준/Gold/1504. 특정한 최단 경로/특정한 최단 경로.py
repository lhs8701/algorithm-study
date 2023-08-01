import sys
import heapq


def relax(distance, v, heap):
    for w, u in graph[v]:
        if distance[u] > distance[v] + w:
            distance[u] = distance[v] + w
            heapq.heappush(heap, (distance[u], u))


def dijkstra(v):
    distance = [int(1e9) for _ in range(N + 1)]
    distance[v] = 0
    heap = [(0, v)]
    heapq.heapify(heap)
    while heap:
        d, v = heapq.heappop(heap)
        if d > distance[v]:
            continue
        relax(distance, v, heap)
    return distance


N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

X, Y = map(int, sys.stdin.readline().rstrip().split())

dist1 = dijkstra(1)
dist2 = dijkstra(N)
dist3 = dijkstra(X)
ans = min(dist1[X] + dist3[Y] + dist2[Y], dist1[Y] + dist3[Y] + dist2[X])
print(-1 if ans >= int(1e9) else ans)
