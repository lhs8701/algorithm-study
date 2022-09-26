import sys
import heapq
N = int(sys.stdin.readline().rstrip())
work = []
for i in range(N):
    d,w = map(int,sys.stdin.readline().rstrip().split())
    work.append((w,d))

work.sort(key=lambda x:(x[1],x[0]))
idx = 1
heap = []

for i in range(0,N):
    if idx <= work[i][1]:
        heapq.heappush(heap,work[i])
        idx+=1
    else:
        temp = heapq.heappop(heap)
        if temp[0] < work[i][0]:
            heapq.heappush(heap,work[i])
        else:
            heapq.heappush(heap,temp)

sum = 0
for i in range(len(heap)):
    sum+=heap[i][0]
print(sum)