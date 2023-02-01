import math
import sys
import heapq


def calc_money(num1, num2):
    digit = len(num1)
    sum = 0
    for i in range(digit):
        sum += (abs(ord(num1[i]) - ord(num2[i]))) ** 2
    return sum


def init_adj(adj, unit):
    for idx, val in unit:
        for i in range(N):
            if unit[i][0] != idx:
                w = calc_money(unit[idx][1], unit[i][1])
                adj[idx].append((w, unit[i][0], unit[i][1]))


def relax(v, edge):
    cost, u, name = edge
    if distance[u] > distance[v] + cost:
        distance[u] = distance[v] + cost
        heapq.heappush(heap, (distance[v] + cost, u, name))


def solve(units, N, source, target):
    global heap, distance
    source -= 1
    target -= 1
    adj = [[] for _ in range(N)]
    distance = [math.inf for _ in range(N)]
    heap = []
    init_adj(adj, units)
    distance[source] = 0
    heapq.heappush(heap, (0, units[source][0], units[source][1]))
    while heap:
        cost, v, name = heapq.heappop(heap)
        for edge in adj[v]:
            relax(v, edge)

    return distance[target]


N = int(sys.stdin.readline().rstrip())
unit = []
for i in range(N):
    unit.append((i, sys.stdin.readline().rstrip()))
source, target = map(int, sys.stdin.readline().rstrip().split())
print(solve(unit, N, source, target))
