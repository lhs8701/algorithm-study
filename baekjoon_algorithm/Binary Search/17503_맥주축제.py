import sys


def check(val):
    temp = [i[0] for i in arr if i[1] <= val]
    return N <= len(temp) and M <= sum(temp[:N])


def binary_search(left, right):
    ans = -1
    arr.sort(key=lambda x: -x[0])
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(K):
    v, c = map(int, sys.stdin.readline().rstrip().split())
    arr.append((v, c))

arr.sort(key=lambda x: x[1])

print(binary_search(arr[0][1], arr[-1][1]))
