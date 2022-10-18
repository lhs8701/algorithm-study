import sys
from collections import deque


def bfs():
    while queue:
        i, j, k = queue.popleft()
        for d in dir:
            ni, nj, nk = i + d[0], j + d[1], k + d[2]
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and box[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
                queue.append((ni, nj, nk))
                box[ni][nj][nk] = box[i][j][k] + 1
                visited[ni][nj][nk] = True


box = []
visited = []
queue = deque()
M, N, H = map(int, sys.stdin.readline().rstrip().split())
dir = [(+1, 0, 0), (-1, 0, 0), (0, +1, 0), (0, -1, 0), (0, 0, +1), (0, 0, -1)]

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    box.append(temp)
    temp = [[False for j in range(M)] for i in range(N)]
    visited.append(temp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
flag = True
max_val = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag = False
            else:
                max_val = max(max_val, box[i][j][k])

if flag:
    print(max_val - 1)
else:
    print(-1)

# import sys
# from collections import deque
#
#
# def bfs(si, sj, sk):
#     queue = deque([(si, sj, sk)])
#     while queue:
#         i, j, k = queue.popleft()
#         for d in dir:
#             ni, nj, nk = i + d[0], j + d[1], k + d[2]
#             if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and (box[ni][nj][nk] == 0 or box[ni][nj][nk] > 1):
#                 if box[ni][nj][nk] != 0:
#                     if box[i][j][k] + 1 < box[ni][nj][nk]:
#                         queue.append((ni, nj, nk))
#                         box[ni][nj][nk] = box[i][j][k] + 1
#                 else:
#                     box[ni][nj][nk] = box[i][j][k] + 1
#                     queue.append((ni, nj, nk))
#
#
# box = []
# M, N, H = map(int, sys.stdin.readline().rstrip().split())
# dir = [(+1, 0, 0), (-1, 0, 0), (0, +1, 0), (0, -1, 0), (0, 0, +1), (0, 0, -1)]
#
# for i in range(H):
#     temp = []
#     for j in range(N):
#         temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
#     box.append(temp)
#
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if box[i][j][k] == 1:
#                 bfs(i, j, k)
#
# flag = True
# max_val = -1
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if box[i][j][k] == 0:
#                 flag = False
#             else:
#                 max_val = max(max_val, box[i][j][k])
#
# if flag:
#     print(max_val - 1)
# else:
#     print(-1)
