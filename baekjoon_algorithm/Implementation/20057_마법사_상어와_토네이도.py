import sys
from collections import deque


def renew_queue(dir_queue, last_dir, last_length):
    if last_dir == 1:
        for i in range(last_length + 1):
            dir_queue.append(2)
        for i in range(last_length + 1):
            dir_queue.append(3)
        return 3
    else:
        for i in range(last_length + 1):
            dir_queue.append(0)
        for i in range(last_length + 1):
            dir_queue.append(1)
        return 1


def control_sand(cur, move_idx):
    move = [(0, -1), (+1, 0), (0, +1), (-1, 0)]
    left_sample = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
    down_sample = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 0, 10, 0], [0, 0, 5, 0, 0]]
    right_sample = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 0, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
    up_sample = [[0, 0, 5, 0, 0], [0, 10, 0, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

    next = tuple(sum(elem) for elem in zip(cur, move[move_idx]))
    a = tuple(sum(elem) for elem in zip(cur, tuple(2 * elem for elem in move[move_idx])))

    original_val = matrix[next[0]][next[1]]
    sum_val = 0
    w = tuple(sum(elem) for elem in zip((2, 2), tuple(elem * -1 for elem in move[move_idx])))
    if move_idx == 0:
        sample = left_sample
    elif move_idx == 1:
        sample = down_sample
    elif move_idx == 2:
        sample = right_sample
    else:
        sample = up_sample

    for i in range(0, 5):
        for j in range(0, 5):
            sum_val += (sample[i][j] * matrix[next[0]][next[1]]) // 100
            matrix[cur[0] + i - w[0]][cur[1] + j - w[1]] += (sample[i][j] * matrix[next[0]][next[1]]) // 100
    matrix[next[0]][next[1]] = 0
    matrix[a[0]][a[1]] += original_val - sum_val


def count():
    ans = 0
    for i in range(N + 4):
        for j in range(N + 4):
            if 0 <= i < 2 or 0 <= j < 2 or N + 2 <= i < N + 4 or N + 2 <= j < N + 4:
                ans += matrix[i][j]
    return ans


def solve():
    move = [(0, -1), (+1, 0), (0, +1), (-1, 0)]
    dir_queue = deque([0, 1])
    last_dir = 1
    last_length = 1
    cur = (N // 2 + 2, N // 2 + 2)
    while cur != (2, 2):
        if not dir_queue:
            last_dir = renew_queue(dir_queue, last_dir, last_length)
            last_length += 1

        move_idx = dir_queue.popleft()
        control_sand(cur, move_idx)
        cur = tuple(sum(elem) for elem in zip(cur, move[move_idx]))

    return count()


N = int(sys.stdin.readline().rstrip())
matrix = [[0 for _ in range(N + 4)], [0 for _ in range(N + 4)]]
for i in range(N):
    temp = [0, 0]
    input_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp + input_arr + temp)
matrix.append([0 for _ in range(N + 4)])
matrix.append([0 for _ in range(N + 4)])
print(solve())

if __name__ == "__main__":
    print("test1")
    N = 5
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 10, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 10
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED , ", "result=", result, ", expected=", expected)

    print("test2")
    N = 5
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 100, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 85
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED")

    print("test3")
    N = 7
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0],
              [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0], [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0], [0, 0, 1, 2, 3, 0, 5, 6, 7, 0, 0],
              [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0], [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0], [0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 139
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED")

    print("test4")
    N = 5
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 200, 300, 400, 200, 0, 0],
              [0, 0, 300, 243, 432, 334, 555, 0, 0], [0, 0, 999, 111, 0, 999, 333, 0, 0],
              [0, 0, 888, 777, 222, 333, 900, 0, 0], [0, 0, 100, 200, 300, 400, 500, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 7501
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED")

    print("test5")
    N = 5
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 100, 0, 0, 0, 0],
              [0, 0, 0, 0, 100, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 100, 0, 0, 0, 0],
              [0, 0, 0, 0, 100, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 283
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED")

    print("test6")
    N = 9
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 193, 483, 223, 482, 858, 274, 847, 283, 748, 0, 0],
              [0, 0, 484, 273, 585, 868, 271, 444, 584, 293, 858, 0, 0],
              [0, 0, 828, 384, 382, 818, 347, 858, 293, 999, 727, 0, 0],
              [0, 0, 818, 384, 727, 373, 636, 141, 234, 589, 991, 0, 0],
              [0, 0, 913, 564, 555, 827, 0, 999, 123, 123, 123, 0, 0],
              [0, 0, 321, 321, 321, 983, 982, 981, 983, 980, 990, 0, 0],
              [0, 0, 908, 105, 270, 173, 147, 148, 850, 992, 113, 0, 0],
              [0, 0, 943, 923, 982, 981, 223, 131, 222, 913, 562, 0, 0],
              [0, 0, 752, 572, 719, 590, 551, 179, 141, 137, 731, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    result = solve()
    expected = 22961
    if result == expected:
        print("SUCCESS")
    else:
        print("FAILED")
