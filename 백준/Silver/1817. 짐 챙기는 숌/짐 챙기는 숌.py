N, M = map(int, input().split())
if N != 0 :
    data = list(map(int, input().split()))
    weigth = 0
    result = 1
    for i in range(N-1, -1, -1) :
        weigth += data[i]
        if weigth > M :
            result += 1
            weigth = data[i]
    print(result)
else :
    print(0)