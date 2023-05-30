import sys
from collections import deque


def D(num):
    return 2 * num % 10000


def S(num):
    return 9999 if num == 0 else num - 1


def L(num):
    temp = str(num)
    prefix = ""
    for _ in range(4 - len(temp)):
        prefix += "0"
    num_list = list(prefix + temp)
    return int("".join(num_list[1:] + num_list[0:1]))


def R(num):
    temp = str(num)
    prefix = ""
    for _ in range(4 - len(temp)):
        prefix += "0"
    num_list = list(prefix + temp)
    return int("".join(num_list[-1:] + num_list[:3]))


def bfs(start):
    visited = [False for _ in range(10000)]
    queue = deque([(start, "")])
    visited[start] = True
    while queue:
        v, seq = queue.popleft()
        if v == B:
            return seq
        for u, commend in graph[v]:
            if not visited[u]:
                queue.append((u, seq + commend))
                visited[u] = True


T = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(10000)]
for i in range(10000):
    graph[i].append((D(i), "D"))
    graph[i].append((S(i), "S"))
    graph[i].append((L(i), "L"))
    graph[i].append((R(i), "R"))
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(A))
