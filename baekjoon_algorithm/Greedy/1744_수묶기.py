import sys
import heapq
#
N = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()
negatives = [i for i in numbers if i <= 0]
positives = [-i for i in numbers if i > 0]
heapq.heapify(negatives)
heapq.heapify(positives)

sum = 0
while len(positives) >= 2:
    num1 = heapq.heappop(positives) * -1
    num2 = heapq.heappop(positives) * -1
    if num1 * num2 >= num1 + num2:
        sum += num1 * num2
    else:
        sum += num1 + num2
if positives:
    sum += heapq.heappop(positives) * -1

while len(negatives) >= 2:
    num1 = heapq.heappop(negatives)
    num2 = heapq.heappop(negatives)
    sum += num1 * num2

if negatives:
    sum += heapq.heappop(negatives)

print(sum)
