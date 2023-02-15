import sys

N = int(sys.stdin.readline().rstrip())
temp = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    temp.append((min(a, b), max(a, b)))

temp.sort()
arr = [elem[1] for elem in temp]
cnt = [1 for i in range(N)]
for i in range(1, N):
    max_val = 0
    for j in range(i):
        if arr[j] <= arr[i]:
            max_val = max(max_val, cnt[j])
    cnt[i] = max_val + 1
print(max(cnt))

# import sys
#
# N = int(sys.stdin.readline().rstrip())
# temp = []
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     temp.append((min(a, b), max(a, b)))
#
# temp.sort()
# arr = [elem[1] for elem in temp]
# cnt = [1 for i in range(N)]
# for i in range(1, N):
#     for j in range(i - 1, -1, -1):
#         if arr[j] <= arr[i]:
#             cnt[i] = cnt[j] + 1
#             break
# print(cnt)
# print(max(cnt))