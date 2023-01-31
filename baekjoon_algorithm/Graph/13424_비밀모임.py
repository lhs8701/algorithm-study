import math
import sys
import heapq


def relax(v, edge):
    global distance, heap
    u = edge[0]
    w = edge[1]
    if distance[u] > distance[v] + w:
        distance[u] = distance[v] + w
        heapq.heappush(heap, (distance[v] + w, u))


def find_min_room(distance_list):
    min_idx = 0
    min_val = math.inf
    for i in range(1, N + 1):
        val = 0
        for j in range(K):
            val += distance_list[j][i]
        if val < min_val:
            min_idx = i
            min_val = val
    return min_idx


def solve(adj, friends):
    global heap, distance
    heap = []
    distance_list = []
    for start in friends:
        distance = [math.inf for _ in range(N + 1)]
        distance[start] = 0
        heapq.heappush(heap, (0, start))
        while heap:
            dist, v = heapq.heappop(heap)
            if distance[v] < dist:
                continue
            for edge in adj[v]:
                relax(v, edge)
        distance_list.append(distance)

    return find_min_room(distance_list)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    K = int(sys.stdin.readline().rstrip())
    friends = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(adj, friends))
