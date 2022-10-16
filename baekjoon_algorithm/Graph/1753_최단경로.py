import sys
import heapq

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())
ans = [sys.maxsize for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
ans[K] = 0
heap = []

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((w, v))

heapq.heappush(heap, (0, K))
while heap:
    cur_w, cur_node = heapq.heappop(heap)
    for adj_w, adj_node in graph[cur_node]:
        if ans[adj_node] > ans[cur_node] + adj_w:
            ans[adj_node] = ans[cur_node] + adj_w
            heapq.heappush(heap, (ans[adj_node], adj_node))

for i in ans[1:]:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)
