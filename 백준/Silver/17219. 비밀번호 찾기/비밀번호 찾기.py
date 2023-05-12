import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dict = dict([])
for _ in range(N):
    key, value = sys.stdin.readline().rstrip().split()
    dict[key] = value
for _ in range(M):
    input = sys.stdin.readline().rstrip()
    print(dict[input])
