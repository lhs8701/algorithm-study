import heapq
import sys

N = int(sys.stdin.readline().rstrip())
arr1 = []
arr2 = []
sum = 0
for i in range(N):
    input = int(sys.stdin.readline().rstrip())
    if input > 0:
        heapq.heappush(arr1, -input)
    else:
        heapq.heappush(arr2, input)

while len(arr1) > 1:
    n1 = -heapq.heappop(arr1)
    n2 = -heapq.heappop(arr1)
    if n1 == 1 or n2 == 1:
        sum += n1 + n2
    else:
        sum += n1 * n2

while len(arr2) > 1:
    n1 = heapq.heappop(arr2)
    n2 = heapq.heappop(arr2)
    sum += n1 * n2

if len(arr1) > 0:
    sum += -heapq.heappop(arr1)
if len(arr2) > 0:
    sum += heapq.heappop(arr2)

print(sum)
