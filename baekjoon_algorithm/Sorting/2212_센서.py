import sys
import heapq

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensor = list(map(int, sys.stdin.readline().rstrip().split()))
sensor.sort()
dict = {}
graph = [[] for i in range(N)]
ans = []
cnt = 0
for i in range(len(sensor)):
    if sensor[i] in dict:
        continue
    else:
        dict[sensor[i]] = cnt
        cnt += 1

arr = []
for i in range(1, len(sensor)):
    heapq.heappush(arr, (sensor[i] - sensor[i - 1], sensor[i - 1], sensor[i], 1))
    j = dict[sensor[i - 1]]
    graph[j].append((sensor[i] - sensor[i - 1], sensor[i - 1], sensor[i], 1))

print(dict)
print(arr)
print(graph)

heapq.heapify(arr)
while arr:
    d, s, e, cnt = heapq.heappop(arr)
    if cnt == K:
        ans.append(d)
    if graph[dict[e]]:
        for i in graph[dict[e]]:
            if i != (d, s, e, cnt):
                heapq.heappush(arr, (i[0] + d, s, i[2], cnt + 1))
    print(arr)

print(min(ans))
