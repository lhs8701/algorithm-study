import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []


def lower_bound(ans, elem):
    left = 0
    right = len(ans)
    while left < right:
        mid = (left + right) // 2
        if ans[mid] < elem:
            left = mid + 1
        else:
            right = mid
    return left


ans.append(arr[0])
for i in range(1, N):
    idx = lower_bound(ans, arr[i])
    if idx >= len(ans):
        ans.append(arr[i])
    else:
        ans[idx] = arr[i]

print(len(ans))