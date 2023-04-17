import sys

N = int(sys.stdin.readline().rstrip())

points = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().rstrip().split())
    points.append((x, y))

points.append((points[0]))
sum_x, sum_y = 0, 0
for i in range(N):
    sum_x += points[i][0] * points[i + 1][1]
    sum_y += points[i][1] * points[i + 1][0]

print(round(abs((sum_x - sum_y) / 2), 1))
