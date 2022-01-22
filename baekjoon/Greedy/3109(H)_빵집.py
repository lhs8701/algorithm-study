import sys

R, C = map(int, sys.stdin.readline().rstrip().split())
road = [['x'] * (C + 2)]
for i in range(R):
    temp = list(sys.stdin.readline().rstrip())
    temp.insert(0, 'x')
    temp.append('x')
    road.append(temp)
road.append(['x'] * (C + 2))

cnt = 0
cur = (1, 1)
row = 1
stack = []
while row <= R:
    i, j = cur
    road[i][j] = 'x'
    if j == C:
        row += 1
        cur = (row, 1)
        cnt += 1
        stack = []
        continue

    if road[i - 1][j + 1] != 'x':
        stack.append(cur)
        cur = (i - 1, j + 1)
        continue
    if road[i][j + 1] != 'x':
        stack.append(cur)
        cur = (i, j + 1)
        continue
    if road[i + 1][j + 1] != 'x':
        stack.append(cur)
        cur = (i + 1, j + 1)
        continue

    if stack:
        cur = stack.pop()
    else:
        row += 1
        cur = (row, 1)

print(cnt)
