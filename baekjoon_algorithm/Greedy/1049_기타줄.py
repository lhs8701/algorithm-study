import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
sets = []
monos = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sets.append(a)
    monos.append(b)

sets.sort()
monos.sort()

print(min((N // 6) * sets[0] + (N % 6) * monos[0], (N // 6 + 1) * sets[0], N * monos[0]))
