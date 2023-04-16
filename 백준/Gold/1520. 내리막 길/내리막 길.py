import sys
import heapq


def solve():
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    visited[0][0] = 1
    heap = []
    for i in range(M):
        for j in range(N):
            heapq.heappush(heap, (matrix[i][j] * -1, i, j))

    visited[0][0] = 1
    while heap:
        height, row, col = heapq.heappop(heap)
        for d_row, d_col in dir:
            u_row, u_col = row + d_row, col + d_col
            if 0 <= u_row < M and 0 <= u_col < N and matrix[row][col] < matrix[u_row][u_col]:
                visited[row][col] += visited[u_row][u_col]

    return visited[M - 1][N - 1]


M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solve())