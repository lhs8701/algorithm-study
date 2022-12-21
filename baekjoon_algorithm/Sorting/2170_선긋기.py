import sys
import heapq

N = int(sys.stdin.readline().rstrip())
lines = set([])
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lines.add((x, y))

START, END = 0, 1
lines = list(lines)
heapq.heapify(lines)
prev = heapq.heappop(lines)
max_end_point = prev[END]
line_length = prev[END] - prev[START]

while lines:
    current = heapq.heappop(lines)
    if current[START] < max_end_point:
        line_length += max(current[END] - max_end_point, 0)
    else:
        line_length += current[END] - current[START]
    max_end_point = max(max_end_point, current[END])

print(line_length)
