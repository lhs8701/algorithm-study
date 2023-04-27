import math
import sys


def root(v):
    while v != parent[v]:
        v = parent[v]
    return v


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


def solve():
    length = len(arr)
    for i in range(length):
        if find(arr[i][0], arr[i][1]):
            return i + 1
        union(arr[i][0], arr[i][1])
    return 0


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
parent = [i for i in range(N)]
depth = [1 for i in range(N)]
for _ in range(M):
    v, u = map(int, sys.stdin.readline().rstrip().split())
    arr.append((v, u))
print(solve())
