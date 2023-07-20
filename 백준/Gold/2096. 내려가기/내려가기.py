import sys

N = int(sys.stdin.readline().rstrip())
matrix = []
dp = [[0, 0, 0] for _ in range(4)]
dp[0][0], dp[0][1], dp[0][2] = map(int, sys.stdin.readline().rstrip().split())
dp[2][0], dp[2][1], dp[2][2] = dp[0][0], dp[0][1], dp[0][2]
for i in range(1, N):
    num0, num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    dp[1][0] = min(dp[0][0], dp[0][1]) + num0
    dp[1][1] = min(dp[0][0], dp[0][1], dp[0][2]) + num1
    dp[1][2] = min(dp[0][1], dp[0][2]) + num2
    dp[3][0] = max(dp[2][0], dp[2][1]) + num0
    dp[3][1] = max(dp[2][0], dp[2][1], dp[2][2]) + num1
    dp[3][2] = max(dp[2][1], dp[2][2]) + num2

    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]
    dp[2][0] = dp[3][0]
    dp[2][1] = dp[3][1]
    dp[2][2] = dp[3][2]

print(max(dp[2]), min(dp[0]))
