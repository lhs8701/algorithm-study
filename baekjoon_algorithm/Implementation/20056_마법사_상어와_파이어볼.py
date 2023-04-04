import sys


def add_dict(dictionary, key, value):
    if dictionary.get(key) == None:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)


def delete_dic(dictionary, key):
    if dictionary.get(key) == None:
        return
    dictionary.pop(key)


def func(r, c, s, d):
    global N
    dir = [(-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1), (-1, -1)]
    return (r + dir[d][0] * s) % N, (c + dir[d][1] * s) % N


def move_fireball(equal_fireballs):
    arr1 = []
    arr2 = []
    for arr in list(equal_fireballs.values()):
        for r, c, m, s, d in arr:
            r_new, c_new = func(r, c, s, d)
            arr1.append((r_new, c_new, m, s, d))
            arr2.append((r, c))

    for r, c in arr2:
        delete_dic(equal_fireballs, (r, c))
    for r, c, m, s, d in arr1:
        add_dict(equal_fireballs, (r, c), (r, c, m, s, d))


def rearrange(r, c, equal_fireballs):
    fbs = equal_fireballs[(r, c)]
    sum_m = fbs[0][2]
    sum_s = fbs[0][3]
    sign = fbs[0][4] % 2
    dir_even = True
    for i in range(1, len(fbs)):
        sum_m += fbs[i][2]
        sum_s += fbs[i][3]
        if fbs[i][4] % 2 != sign:
            dir_even = False
    m_new = sum_m // 5
    s_new = sum_s // len(fbs)
    start = 0 if dir_even else 1

    equal_fireballs.pop((r, c))
    if m_new == 0:
        return
    for i in range(start, 8, 2):
        add_dict(equal_fireballs, (r, c), (r, c, m_new, s_new, i))


def check(equal_fireballs):
    arr = []
    for key, value in equal_fireballs.items():
        if len(value) >= 2:
            arr.append(key)
    return arr


def solve(fireballs):
    ans = 0
    equal_fireballs = {}
    for r, c, m, s, d in fireballs:
        add_dict(equal_fireballs, (r, c), (r, c, m, s, d))
    for _ in range(K):
        move_fireball(equal_fireballs)
        next = check(equal_fireballs)
        for r, c in next:
            rearrange(r, c, equal_fireballs)

    for elem in list(equal_fireballs.values()):
        for _, _, m, _, _ in elem:
            ans += m
    return ans


N, M, K = map(int, sys.stdin.readline().rstrip().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().rstrip().split())
    fireballs.append((r - 1, c - 1, m, s, d))
print(solve(fireballs))

if __name__ == "__main__":
    print("test 1 ")
    N = 4
    M = 2
    K = 1
    test = [(0, 0, 5, 2, 2), (0, 3, 7, 1, 6)]
    result = solve(test)
    expected = 8
    if result == expected:
        print("SUCCESS")
    else:
        print("FAIL")

    print("test 2 ", end='')
    N = 4
    M = 2
    K = 2
    test = [(0, 0, 5, 2, 2), (0, 3, 7, 1, 6)]
    result = solve(test)
    expected = 8
    if result == expected:
        print("SUCCESS")
    else:
        print("FAIL")

    print("test 3 ", end='')
    N = 4
    M = 2
    K = 3
    test = [(0, 0, 5, 2, 2), (0, 3, 7, 1, 6)]
    result = solve(test)
    expected = 0
    if result == expected:
        print("SUCCESS")
    else:
        print("FAIL")

    print("test 4 ", end='')
    N = 7
    M = 5
    K = 3
    test = [(1, 3, 5, 2, 4), (2, 3, 5, 2, 6), (5, 2, 9, 1, 7), (6, 2, 1, 3, 5), (4, 4, 2, 4, 2)]
    result = solve(test)
    expected = 9
    if result == expected:
        print("SUCCESS")
    else:
        print("FAIL")
