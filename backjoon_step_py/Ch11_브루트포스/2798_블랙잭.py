import sys
import itertools

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
comb = list(itertools.combinations(arr, 3))
max = -1
for elem in comb:
    if sum(elem) <= M and max < sum(elem):
        max = sum(elem)
print(max)
