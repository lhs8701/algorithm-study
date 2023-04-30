import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
print('Yes' if 100 * N >= M else 'No')