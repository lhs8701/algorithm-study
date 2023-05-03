import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
dict = dict([])
problem = []
for i in range(N):
    input = sys.stdin.readline().rstrip()
    arr.append(input)
    dict[input] = i

for i in range(M):
    problem.append(sys.stdin.readline().rstrip())

for i in problem:
    if i.isdigit():
        print(arr[int(i) - 1])
    else:
        print(dict[i] + 1)
