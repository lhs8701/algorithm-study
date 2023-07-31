import sys


def union(v, u):
    rootV = root(v)
    rootU = root(u)
    parent[rootU] = parent[rootV]


def root(v):
    while parent[v] != v:
        v = parent[v]
    return v


N, M = map(int, sys.stdin.readline().rstrip().split())
temp = list(map(int, sys.stdin.readline().rstrip().split()))
awareNumber, knowingSet = temp[0], temp[1:]
party = []
parent = [i for i in range(N + 1)]
cnt = 0

for i in range(M):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    party.append(temp[1:])

for i in range(M):
    party[i].sort()
    awareMember = None
    for j in range(len(party[i])):
        member = party[i][j]
        if root(member) in knowingSet:
            awareMember = member
            break
    v = party[i][0] if awareMember is None else awareMember
    for j in range(len(party[i])):
        member = party[i][j]
        union(v, member)

for i in range(M):
    success = True
    for j in range(len(party[i])):
        member = party[i][j]
        if root(member) in knowingSet:
            success = False
            break
    if success:
        cnt += 1

print(cnt)
