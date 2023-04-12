import sys
from collections import deque


def bfs(level):
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]  # [찬스 안씀, 찬스 씀]
    dir = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
    if matrix[0][0] > level:
        return False
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = True
    while queue:
        v_row, v_col, used = queue.popleft()
        for d_row, d_col in dir:
            u_row, u_col = v_row + d_row, v_col + d_col
            if 0 <= u_row < n and 0 <= u_col < m and not visited[u_row][u_col][used]:
                if matrix[u_row][u_col] <= level:
                    visited[u_row][u_col][used] = True
                    queue.append((u_row, u_col, used))
                else:
                    if used == 0 and 0 <= u_row + d_row < n and 0 <= u_col + d_col < m and matrix[u_row + d_row][
                        u_col + d_col] <= level:
                        visited[u_row + d_row][u_col + d_col][1] = True
                        queue.append((u_row + d_row, u_col + d_col, 1))
    return visited[n - 1][m - 1][0] or visited[n - 1][m - 1][1]


def binary_search(left, right):
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if bfs(levels[mid]):
            ans = levels[mid]
            right = mid - 1
        else:
            left = mid + 1
    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())

matrix = []
level_set = set()
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp)
    level_set.update(set(temp))
levels = list(level_set)
levels.sort()
print(binary_search(0, len(levels) - 1))
