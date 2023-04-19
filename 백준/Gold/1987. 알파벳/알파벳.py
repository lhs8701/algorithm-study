import sys

sys.setrecursionlimit(10000)


def dfs(vr, vc, visited, alpha):
    global ans, dir
    ans = max(ans, visited[vr][vc])
    for dr, dc in dir:
        ur, uc = vr + dr, vc + dc
        if 0 <= ur < R and 0 <= uc < C and visited[ur][uc] == 0 and not alpha[ord(matrix[ur][uc]) - ord('A')]:
            alpha[ord(matrix[ur][uc]) - ord('A')] = True
            visited[ur][uc] = visited[vr][vc] + 1
            dfs(ur, uc, visited, alpha)
            visited[ur][uc] = 0
            alpha[ord(matrix[ur][uc]) - ord('A')] = False


R, C = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for i in range(R):
    matrix.append(list(str(sys.stdin.readline().rstrip())))
visited = [[0 for _ in range(C)] for _ in range(R)]
dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
alpha = [False for _ in range(26)]
ans = -1

visited[0][0] = 1
alpha[ord(matrix[0][0]) - ord('A')] = True
dfs(0, 0, visited, alpha)
print(ans)
