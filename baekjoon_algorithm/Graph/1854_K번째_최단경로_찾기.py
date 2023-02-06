import sys


def solve(adj, n, k):
    pass


n, m, k = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((c, b))

print(solve(adj, n, k))
