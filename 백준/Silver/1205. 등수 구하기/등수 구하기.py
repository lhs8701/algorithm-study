import sys

read = lambda: sys.stdin.readline().rstrip()

N, new, P = map(int, read().split())

score = []

if N:
	score = list(map(int, read().split()))
	score.append(new)
	score.sort(reverse=True)
	rank = score.index(new) + 1
	if rank > P:
		print(-1)
	else:
		if N == P and new == score[-1]:
			print(-1)
		else:
			print(rank)
else:
	print(1)