import sys
from collections import deque


def bfs(start):
    visited = [False for _ in range(101)]
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        if v == 100:
            break
        if v in item:
            r = v
            while r in item:
                r = item[r]
            cnt[r] = cnt[v]
            v = r
        for d in range(1, 7):
            u = v + d
            if u <= 100 and not visited[u]:
                cnt[u] = cnt[v] + 1
                visited[u] = True
                queue.append(u)
    return cnt[100]


N, M = map(int, sys.stdin.readline().rstrip().split())
item = {}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    item[x] = y

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    item[x] = y

cnt = [0 for _ in range(101)]
cnt[1] = 0
print(bfs(1))
