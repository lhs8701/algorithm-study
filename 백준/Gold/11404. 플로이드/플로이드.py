import math
import sys


def relax():
    pass


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dist = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    dist[a][b] = min(dist[a][b], c)

for i in range(n + 1):
    dist[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != math.inf else 0, end=' ')
    print()
