
N = input()
arr = []
arr = sorted(N)
arr = list(map(int,arr))
if arr[0] != 0 or sum(arr)%3 != 0:
    print(-1)
else:
    arr.reverse()
    print("".join(list(map(str,arr))))
