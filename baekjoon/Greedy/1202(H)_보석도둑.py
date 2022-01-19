
import sys
import heapq

N,K = map(int,sys.stdin.readline().rstrip().split())
jew = []
bag = []
for i in range(N):
    M,V = map(int,sys.stdin.readline().rstrip().split())
    jew.append((V,M))
for i in range(K):
    bag.append(int(sys.stdin.readline().rstrip()))

bag.sort()
jew.sort(key=lambda x:x[1])

sum = 0
heap = []

j = 0
for i in range(K):
    while j<N and jew[j][1]<=bag[i] :
        jew[j] = list(jew[j])
        jew[j][0]*=-1
        jew[j] = tuple(jew[j])
        heapq.heappush(heap, jew[j])
        j+=1
    if len(heap) != 0:
        temp = heapq.heappop(heap)
        sum+= -temp[0]

print(sum)