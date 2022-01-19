import sys
from itertools import combinations

def dist(d1, d2):
    return abs(d1[0]-d2[0]) + abs(d1[1]-d2[1])

N,M = map(int,sys.stdin.readline().rstrip().split())
block = []
house = []
store = []
for i in range(N):
    block.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(N):
        if block[i][j] == 1:
            house.append((i,j))
        if block[i][j] == 2:
            store.append((i,j))

ans = sys.maxsize
for select in range(1,M+1):
    sum = 0
    arr = list(combinations(store,select))
    m2 = sys.maxsize
    for i in range(len(arr)):
        sum = 0
        for j in range(len(house)):
            m1 = sys.maxsize
            for k in range(select):
                m1 = min(dist(house[j], arr[i][k]), m1)
            sum += m1
        m2 = min(sum,m2)
    ans = min(ans, m2)

print(ans)