import sys
from collections import deque


def solve():
    queue = deque([])
    for i in range(1, N + 1):
        if pre[i] == 0:
            queue.append(i)

    while pre[W] > 0:
        v = queue.popleft()
        for u in suc[v]:
            time[u] = max(time[v] + weight[v], time[u])
            pre[u] -= 1
            if pre[u] == 0:
                queue.append(u)
    return time[W] + weight[W]


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    weight = list(map(int, sys.stdin.readline().rstrip().split()))
    weight.insert(0, -1)
    suc = [[] for _ in range(N + 1)]
    pre = [0 for _ in range(N + 1)]
    time = [0 for _ in range(N + 1)]
    for _ in range(K):
        v, u = map(int, sys.stdin.readline().rstrip().split())
        suc[v].append(u)
        pre[u] += 1
    W = int(sys.stdin.readline().rstrip())
    print(solve())
