import math
import sys

N = int(sys.stdin.readline().rstrip())
edge = list(map(int, sys.stdin.readline().rstrip().split()))
vertex = list(map(int, sys.stdin.readline().rstrip().split()))

min_val = math.inf
sum = 0
for i in range(N - 1):
    min_val = min(min_val, vertex[i])
    sum += edge[i] * min_val

print(sum)
