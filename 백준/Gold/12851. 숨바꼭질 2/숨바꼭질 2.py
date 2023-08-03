import sys
from collections import deque


def bfs(N):
    TIME, WAYS = 0, 1
    record = [[int(1e9), 0] for _ in range(100001)]
    record[N][TIME] = 0
    record[N][WAYS] = 1
    queue = deque([N])

    while queue:
        v = queue.popleft()
        next_v = [v - 1, v + 1, 2 * v]
        for nv in next_v:
            if 0 <= nv <= 100000 and record[v][TIME] + 1 <= record[nv][TIME]:
                record[nv][TIME] = record[v][TIME] + 1
                record[nv][WAYS] += 1
                queue.append(nv)
        next_v.clear()

    return record[K][TIME], record[K][WAYS]


N, K = map(int, sys.stdin.readline().rstrip().split())
time, ways = bfs(N)
print(time)
print(ways)
