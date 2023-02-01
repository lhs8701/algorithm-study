import math
import sys
import heapq


def relax(v, edge):
    w, u = edge
    if distance[u] > distance[v] + w:
        distance[u] = distance[v] + w
        edge_to[u] = v
        heapq.heappush(heap, (distance[u], u))


def get_shortest_path(adj, excluded, N):
    global distance, edge_to, heap
    distance = [math.inf for _ in range(N + 1)]
    edge_to = [-1 for _ in range(N + 1)]
    heap = []

    # 시작 정점 초기화
    heapq.heappush(heap, (0, 1))
    distance[1] = 0
    edge_to[1] = 1

    while heap:
        cost, v = heapq.heappop(heap)
        for edge in adj[v]:
            if edge != excluded:
                relax(v, edge)

    return distance[N], edge_to


def solve(adj, N, M):
    shortest_path_edges = []

    # 실제 최단경로의 길이를 구한다.
    real_shortest_distance, edge_to = get_shortest_path(adj, (-1, -1), N)

    # 최단 경로를 이루는 엣지를 구한다.
    cur = N
    while True:
        prev = edge_to[cur]
        if prev == cur: break
        shortest_path_edges.append((prev, cur))
        cur = prev

    # 최단 경로 중 하나의 엣지를 제거한 최단경로의 길이를 구한다.
    max_val = 0
    for elem in shortest_path_edges:
        # 제거할 엣지를 선택한다.
        edge = -1
        for i in range(len(adj[elem[0]])):
            if adj[elem[0]][i][1] == elem[1]:
                edge = adj[elem[0]][i]
                break
        limited_shortest_distance, temp = get_shortest_path(adj, edge, N)
        if limited_shortest_distance == math.inf:
            return -1
        max_val = max(max_val, limited_shortest_distance)

    return max_val - real_shortest_distance


N, M = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((t, b))
    adj[b].append((t, a))

print(solve(adj, N, M))

if __name__ == "__main__":
    # test 1
    test = [[], [(1, 2), (3, 4)], [(1, 1), (2, 3)], [(1, 6), (2, 2), (1, 4)], [(3, 1), (1, 5), (1, 3)],
            [(1, 4), (2, 6)], [(1, 3), (2, 5)]]
    expected = 2
    result = solve(test, 6, 7)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)

    # test 2
    test = [[], [(1, 2), (8, 5), (9, 7)], [(1, 1), (2, 5)], [(4, 4), (3, 6), (5, 8)], [(4, 3), (10, 6), (11, 8)],
            [(8, 1), (2, 2), (6, 6), (7, 7)], [(3, 3), (10, 4), (6, 5)], [(9, 1), (7, 5)], [(5, 3), (11, 4)]]
    expected = -1
    result = solve(test, 8, 11)
    if result != expected:
        print("test 2 fail, result:", result, ", expected:", expected)
