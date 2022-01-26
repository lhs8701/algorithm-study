import sys
import itertools

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

val = sum(arr) - 100
nCr = itertools.combinations(arr, 2)
for element in nCr:
    if sum(element) == val:
        arr.remove(element[0])
        arr.remove(element[1])
        break
for i in arr:
    print(i)
