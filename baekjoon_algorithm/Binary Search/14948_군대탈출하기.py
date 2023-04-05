import sys

sys.setrecursionlimit(10000)


def check(limit, cur_row, cur_col, visited, use):
    if cur_row == n - 1 and cur_col == m - 1:
        return True

    visited[cur_row][cur_col] = True
    for d_row, d_col in dir:
        next_row, next_col = cur_row + d_row, cur_col + d_col
        if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col] and matrix[next_row][
            next_col] <= limit:
            result = check(limit, next_row, next_col, visited, use)
            if result:
                return True
            visited[next_row][next_col] = False
    if not use:
        for d_row, d_col in dir:
            next_row, next_col = cur_row + 2 * d_row, cur_col + 2 * d_col
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col] and matrix[next_row][
                next_col] <= limit:
                result = check(limit, next_row, next_col, visited, True)
                if result:
                    return True
                visited[next_row][next_col] = False

    return False


def binary_search(left, right):
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        visited = [[False for _ in range(m)] for _ in range(n)]
        if check(levels[mid], 0, 0, visited, False):
            ans = levels[mid]
            right = mid - 1
        else:
            left = mid + 1
    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())

matrix = []
dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
level_set = set()
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp)
    level_set.update(set(temp))
levels = list(level_set)
levels.sort()

print(binary_search(0, len(levels) - 1))
