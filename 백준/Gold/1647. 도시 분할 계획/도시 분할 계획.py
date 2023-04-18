import sys
import heapq


def root(v):
    r = v
    while r != parent[r]:
        r = parent[r]
    return r


def union(v, u):
    root_v = root(v)
    root_u = root(u)
    if depth[root_v] < depth[root_u]:
        parent[root_v] = root_u
    elif depth[root_v] == depth[root_u]:
        parent[root_u] = root_v
        depth[root_v] += 1
    else:
        parent[root_u] = root_v


def find(v, u):
    return root(v) == root(u)


N, M = map(int, sys.stdin.readline().rstrip().split())
edges = []
for i in range(M):
    v, u, w = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(edges, (w, v, u))

parent = [i for i in range(N + 1)]
depth = [1 for i in range(N + 1)]
ans = 0
cnt = 0

while cnt < N - 2:
    w, v, u = heapq.heappop(edges)
    if not find(v, u):
        union(v, u)
        cnt += 1
        ans += w

print(ans)
