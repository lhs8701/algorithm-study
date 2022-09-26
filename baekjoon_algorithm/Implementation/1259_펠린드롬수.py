import sys

while True:
    flag = True
    Arr = list(sys.stdin.readline().rstrip())
    if Arr[0] == '0':
        break
    l = len(Arr)
    for i in range(l//2):
        j = l-1 - i
        if Arr[i] != Arr[j]:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")