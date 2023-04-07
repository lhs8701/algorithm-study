import sys
from collections import deque


def rotate(l):
    sub_len = 2 ** l
    full_len = 2 ** N
    rotated_sub_list = []
    for i in range(0, full_len, sub_len):
        for j in range(0, full_len, sub_len):
            sub = [row[j:j + sub_len] for row in matrix[i:i + sub_len]]
            rotated = list(zip(*sub[::-1]))
            rotated_sub_list.append(rotated)
    for i in range((full_len // sub_len) ** 2):
        row = (i // (full_len // sub_len)) * sub_len
        col = (i % (full_len // sub_len)) * sub_len
        for j in range(sub_len):
            for k in range(sub_len):
                matrix[row + j][col + k] = rotated_sub_list[i][j][k]


def decrease_ice():
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    arr = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for dr, dc in dir:
                if 0 <= i + dr < 2 ** N and 0 <= j + dc < 2 ** N and matrix[i + dr][j + dc] > 0:
                    cnt += 1
            if cnt < 3 and matrix[i][j] > 0:
                arr.append((i, j))

    while arr:
        r, c = arr.pop()
        matrix[r][c] -= 1


def bfs(start):
    global visited
    global sum_val
    global max_component_size
    dir = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    queue = deque([(start[0], start[1])])
    visited[start[0]][start[1]] = True
    sum_val += matrix[start[0]][start[1]]
    cnt = 1
    while queue:
        vr, vc = queue.popleft()
        for dr, dc in dir:
            ur, uc = vr + dr, vc + dc
            if 0 <= ur < 2 ** N and 0 <= uc < 2 ** N and not visited[ur][uc] and matrix[ur][uc] != 0:
                sum_val += matrix[ur][uc]
                cnt += 1
                visited[ur][uc] = True
                queue.append((ur, uc))
    return cnt


def solve():
    global visited, sum_val, max_component_size
    queue_l = deque(L)
    for _ in range(Q):
        l = queue_l.popleft()
        rotate(l)
        decrease_ice()

    visited = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
    sum_val = 0
    max_component_size = 0
    for i in range(2 ** N):
        for j in range(2 ** N):
            if not visited[i][j] and matrix[i][j] != 0:
                max_component_size = max(bfs((i, j)), max_component_size)

    return sum_val, max_component_size


N, Q = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for i in range(2 ** N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

L = list(map(int, sys.stdin.readline().rstrip().split()))
ans1, ans2 = solve()
print(ans1)
print(ans2)

if __name__ == "__main__":
    print("test 1")
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
    N = 3
    Q = 1
    L = [1]
    result1, result2 = solve()
    expected1, expected2 = 284, 64
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))

    print("test 2")
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
    N = 3
    Q = 2
    L = [1, 2]
    result1, result2 = solve()
    expected1, expected2 = 280, 64
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))

    print("test 3")
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
    N = 3
    Q = 5
    L = [1, 2, 0, 3, 2]
    result1, result2 = solve()
    expected1, expected2 = 268, 64
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))

    print("test 4")
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
    N = 3
    Q = 10
    L = [1, 2, 0, 3, 2, 1, 2, 3, 2, 3]
    result1, result2 = solve()
    expected1, expected2 = 248, 62
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))

    print("test 5")
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
    N = 3
    Q = 10
    L = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    result1, result2 = solve()
    expected1, expected2 = 246, 60
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))

    print("test 6")
    matrix = [[1, 0, 3, 4, 5, 6, 7, 0], [8, 0, 6, 5, 4, 3, 2, 1], [1, 2, 0, 4, 5, 6, 7, 0], [8, 7, 6, 5, 4, 3, 2, 1],
              [1, 2, 3, 4, 0, 6, 7, 0], [8, 7, 0, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 0], [0, 7, 0, 5, 4, 3, 2, 1]]
    N = 3
    Q = 10
    L = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    result1, result2 = solve()
    expected1, expected2 = 37, 9
    if result1 == expected1 and result2 == expected2:
        print("SUCCESS")
    else:
        print("FAIL: expected= {} {} | result= {} {}".format(expected1, expected2, result1, result2))
