import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())


def bfs(N):
    global K
    nums = [-1] * 200002
    queue = deque([N])
    nums[N] = 0
    while queue:
        n = queue.popleft()
        if n > 100000 or n < 0:
            continue
        if n == K:
            return nums[n]

        if nums[n - 1] == -1:
            queue.append(n - 1)
            nums[n - 1] = nums[n] + 1
        if nums[n + 1] == -1:
            queue.append(n + 1)
            nums[n + 1] = nums[n] + 1
        if nums[2 * n] == -1:
            queue.append(2 * n)
            nums[2 * n] = nums[n] + 1


print(bfs(N))
