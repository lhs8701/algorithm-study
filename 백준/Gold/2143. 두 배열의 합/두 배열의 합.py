import sys

T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rstrip().split()))

len_a = len(A)
len_b = len(B)
dp_a = [0 for i in range(len_a)]
dp_b = [0 for i in range(len_b)]
dp_a[0] = A[0]
for i in range(1, len_a):
    dp_a[i] = dp_a[i - 1] + A[i]
dp_b[0] = B[0]
for i in range(1, len_b):
    dp_b[i] = dp_b[i - 1] + B[i]

cnt = 0
dict_a = dict([])
dict_b = dict([])
for l in range(n):
    for r in range(l, n):
        key = dp_a[r] - dp_a[l] + A[l]
        if key in dict_a:
            dict_a[key] += 1
        else:
            dict_a[key] = 1

for l in range(m):
    for r in range(l, m):
        key = dp_b[r] - dp_b[l] + B[l]
        if key in dict_b:
            dict_b[key] += 1
        else:
            dict_b[key] = 1

for key, value in dict_a.items():
    if T - key in dict_b:
        cnt += value * dict_b[T - key]

print(cnt)
