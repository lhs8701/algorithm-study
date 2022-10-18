import sys


def dfs(graph, visited, v):
    visited[v[0]][v[1]] = True

    for d in dir:
        next_x, next_y = v[0] + d[0], v[1] + d[1]
        if 0 <= next_x < h and 0 <= next_y < w and graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
            dfs(graph, visited, (next_x, next_y))


def bfs(graph, visited, start):
    queue = [start]
    visited[start[0]][start[1]] = True

    while queue:
        vx, vy = queue.pop(0)
        for d in dir:
            next_x, next_y = vx + d[0], vy + d[1]
            if 0 <= next_x < h and 0 <= next_y < w and graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


dir = [(-1, 0), (0, +1), (+1, 0), (0, -1), (+1, +1), (+1, -1), (-1, +1), (-1, -1)]
while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt = 0
    visited = [[False for j in range(w)] for i in range(h)]
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph, visited, (i, j))
                cnt += 1
            # if graph[i][j] == 1 and not visited[i][j]:
            #     dfs(graph, visited, (i, j))
            #     cnt += 1
    print(cnt)
