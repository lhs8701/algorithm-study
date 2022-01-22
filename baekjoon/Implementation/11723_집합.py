import sys

M = int(sys.stdin.readline().rstrip())

num = [0] * 21
numEmpty = [0] * 21
numFull = [1] * 21

for i in range(M):
    comm = sys.stdin.readline().rstrip().split()
    if len(comm) == 1:
        if comm[0] == "all":
            num = numFull
        else:
            num = numEmpty
    else:
        x = int(comm[1])
        if comm[0] == "add":
            num[x] = 1
        elif comm[0] == "remove":
            num[x] = 0
        elif comm[0] == "check":
            if num[x] == 1:
                print(1)
            else:
                print(0)
        elif comm[0] == "toggle":
            if num[x] == 1:
                num[x] = 0
            else:
                num[x] = 1
