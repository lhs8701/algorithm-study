import math
import sys
from collections import deque


def bfs(start_r, start_c):
    global cnt
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = True
    ans = []
    while queue:
        v_r, v_c, t = queue.popleft()
        if 0 < matrix[v_r][v_c] < cur:
            ans.append((v_r, v_c, t))
        for dr, dc in dir:
            u_r, u_c = v_r + dr, v_c + dc
            if 0 <= u_r < N and 0 <= u_c < N and not visited[u_r][u_c] and matrix[u_r][u_c] <= cur:
                queue.append((u_r, u_c, t + 1))
                visited[u_r][u_c] = True
    return ans


def is_available(cur):
    arr = fish[:min(cur, 7)]
    for i in arr:
        if i > 0:
            return True
    return False


N = int(sys.stdin.readline().rstrip())
matrix = []
r, c = -1, -1
fish = [0 for _ in range(7)]
dir = [(-1, 0), (0, -1), (0, +1), (+1, 0)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if temp[j] == 9:
            r, c = i, j
            temp[j] = 0
        else:
            fish[temp[j]] += 1
    matrix.append(temp)
fish[0] = 0

cur = 2
cnt = 0
time = 0
while is_available(cur):
    arr = bfs(r, c)
    if not arr:
        break
    arr.sort(key=lambda x: (x[2], x[0], x[1]))
    elem = arr[0]
    fish[matrix[elem[0]][elem[1]]] -= 1
    matrix[elem[0]][elem[1]] = 0
    r, c, t = elem
    cnt += 1
    time += t
    if cnt == cur:
        cnt = 0
        cur += 1
print(time)
