import sys


def push(prev, cur):
    if prev > cur:
        return 0
    else:
        return cur - prev + 1


def solve(arr, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, 2 * n - 1):
        start = i // n * (i % n + 1)
        for j in range(start, i + 1 - start):
            cur_x = j
            cur_y = i - j
            right_path, down_path = sys.maxsize, sys.maxsize
            if cur_x > 0:
                down_path = dp[cur_x - 1][cur_y] + push(arr[cur_x - 1][cur_y], arr[cur_x][cur_y])
            if cur_y > 0:
                right_path = dp[cur_x][cur_y - 1] + push(arr[cur_x][cur_y - 1], arr[cur_x][cur_y])
            dp[cur_x][cur_y] = min(right_path, down_path)

    return dp[n - 1][n - 1]


n = int(sys.stdin.readline().rstrip())
mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solve(mat, n))

if __name__ == "__main__":
    # test 1
    arr = [[5, 2, 4, 3], [6, 5, 1, 2], [3, 4, 5, 3], [7, 4, 3, 1]]
    expected = 3
    result = solve(arr, 4)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)

    # test 2
    arr = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    expected = 8
    result = solve(arr, 5)
    if result != expected:
        print("test 2 fail, result:", result, ", expected:", expected)
