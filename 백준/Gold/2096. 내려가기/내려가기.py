import sys

N = int(sys.stdin.readline().rstrip())
maxDp = [0, 0, 0]
minDp = [0, 0, 0]
maxDp[0], maxDp[1], maxDp[2] = map(int, sys.stdin.readline().rstrip().split())
minDp[0], minDp[1], minDp[2] = maxDp[0], maxDp[1], maxDp[2]
for i in range(1, N):
    num0, num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    maxDp = [max(maxDp[0], maxDp[1]) + num0, max(maxDp[0], maxDp[1], maxDp[2]) + num1, max(maxDp[1], maxDp[2]) + num2]
    minDp = [min(minDp[0], minDp[1]) + num0, min(minDp[0], minDp[1], minDp[2]) + num1, min(minDp[1], minDp[2]) + num2]

print(max(maxDp), min(minDp))
