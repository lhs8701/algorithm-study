import math
import sys
import heapq

N, M, B = map(int, sys.stdin.readline().rstrip().split())
heights = []
counts = [0 for _ in range(257)]
heap = []
for i in range(N):
    heights.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(M):
        counts[heights[i][j]] += 1

for i in range(257):
    heapq.heappush(heap, (counts[i] * -1, i))

ans_time = math.inf
ans_height = -1

while heap:
    n, h = heapq.heappop(heap)
    num_cut = 0
    for i in range(h + 1, 257):
        num_cut += (i - h) * counts[i]
    num_need = 0
    for i in range(0, h):
        num_need += (h - i) * counts[i]
    if B + num_cut >= num_need:
        time = num_cut * 2 + num_need
        if ans_time > time:
            ans_time = time
            ans_height = h
        elif ans_time == time:
            if ans_height < h:
                ans_height = h

print(ans_time, ans_height)
