while True:
    c_list = []
    N = input()
    if N == '0':
        break
    for i in N:
        c_list.append(i)

    tot = 0
    for i in c_list:
        tot += 1
        if i == '0':
            tot += 4
        elif i == '1':
            tot += 2
        else:
            tot += 3
    tot += 1
    print(tot)