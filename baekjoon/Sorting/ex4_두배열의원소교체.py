import sys
import heapq
N,K = map(int,sys.stdin.readline().rstrip().split())
A = list(map(int,sys.stdin.readline().rstrip().split()))
B = list(map(int,sys.stdin.readline().rstrip().split()))
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break
print(sum(A))