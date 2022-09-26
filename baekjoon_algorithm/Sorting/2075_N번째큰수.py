# import sys
# import heapq
#
# N = int(sys.stdin.readline().rstrip())
# heap = list(map(int, sys.stdin.readline().rstrip().split()))
# heapq.heapify(heap)
# cnt = 0
# ans = -1
# for i in range(N - 1):
#     temp = list(map(int, sys.stdin.readline().rstrip().split()))
#     minVal = min(temp)
#     while heap:
#         if heap[0] < minVal:
#             cnt += 1
#             n = heapq.heappop(heap)
#             if cnt == N * N - N + 1:
#                 ans = n
#                 break
#         else:
#             break
#     if ans != -1:
#         break
#     for j in range(N):
#         heapq.heappush(heap, temp[j])
#
# if ans == -1:
#     while heap:
#         cnt += 1
#         n = heapq.heappop(heap)
#         if cnt == N * N - N + 1:
#             ans = n
#             break
#
# print(ans)

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = list(map(int, sys.stdin.readline().rstrip().split()))
heapq.heapify(heap)
for i in range(N - 1):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if heap[0] < temp[j]:
            heapq.heappush(heap, temp[j])
            heapq.heappop(heap)

print(heap[0])
