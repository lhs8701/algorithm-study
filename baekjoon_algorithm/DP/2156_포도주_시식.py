import sys


def solve(arr, n):
    dp = [[0, 0] for _ in range(n + 2)]
    dp[0][0], dp[0][1] = 0, 0
    dp[1][0], dp[1][1] = 0, 0
    max_val = -1
    for i in range(2, n + 2):
        idx = i - 2
        dp[i][0] = max(max(dp[i - 2]) + arr[idx], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][0] + arr[idx], dp[i - 1][1])
        if max_val < max(dp[i][0], dp[i][1]):
            max_val = max(dp[i][0], dp[i][1])

    return max_val


n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

print(solve(arr, n))

if __name__ == "__main__":
    # test 1
    test = [6, 10, 13, 9, 8, 1]
    expected = 33
    result = solve(test, 6)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)

    # test 2
    test = [999, 999, 1, 1, 999, 999]
    expected = 3996
    result = solve(test, 6)
    if result != expected:
        print("test 2 fail, result:", result, ", expected:", expected)
