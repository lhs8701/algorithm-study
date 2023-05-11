import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    minQ, maxQ = [], []
    deleted = [True] * k  
    for i in range(k):
        com, n = input().split()
        n = int(n)
        if com == 'I':
            heapq.heappush(minQ, (n, i))
            heapq.heappush(maxQ, (-n, i))
            deleted[i] = False
        else:
            if n == 1:
                while maxQ and deleted[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    deleted[maxQ[0][1]] = True
                    heapq.heappop(maxQ)
            else:
                while minQ and deleted[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heapq.heappop(minQ)

    while minQ and deleted[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and deleted[maxQ[0][1]]:
        heapq.heappop(maxQ)
    
    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')