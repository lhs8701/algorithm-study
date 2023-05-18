import sys

sys.setrecursionlimit(10000)


def dfs(v, visited):
    for u in range(N):
        if visited[u] == 0 and matrix[v][u] == 1:
            visited[u] = 1
            dfs(u, visited)


N = int(sys.stdin.readline().rstrip())
matrix = []
answer = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i, visited)
    for j in visited:
        print(j, end=' ')
    print()
