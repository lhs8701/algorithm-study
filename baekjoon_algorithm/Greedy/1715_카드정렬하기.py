import sys
import heapq
N = int(sys.stdin.readline().rstrip())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

sum=0
for i in range(N-1):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    sum+= (n1+n2)
    heapq.heappush(heap,n1+n2)
print(sum)
