from itertools import combinations
N, M, K = map(int, input().split())
cntA = cntB = 0
for combA in combinations(range(N), M):
    for combB in combinations(range(N), M):
        cntA += 1
        if len(set(combA)&set(combB)) >= K: cntB += 1

print(cntB/cntA)