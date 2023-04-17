def solution(emergency):
    length = len(emergency)
    arr = [(emergency[i], i) for i in range(length)]
    ans = [0 for _ in range(length)]
    arr.sort(key=lambda x:-x[0])
    print(arr)
    for i in range(len(emergency)):
        ans[arr[i][1]] = i+1
    return ans