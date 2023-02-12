import sys


def solve(parent, N):
    global early_adopter
    next = set([])
    vertex = set([i for i in range(1, N + 1)])
    non_leaf = set(parent)
    leaf = vertex.difference(non_leaf)
    early_adopter = [0 for _ in range(N + 1)]
    while leaf:
        for l in leaf:
            p = parent[l]
            if p != -1:
                next.add(p)

            if early_adopter[l] == 0:
                if p == -1:
                    early_adopter[l] = 1
                else:
                    early_adopter[p] = 1
            elif early_adopter[l] == 1 and p != -1 and early_adopter[p] == 0:
                early_adopter[p] = 2
            elif early_adopter[l] == 2 and p != -1:
                early_adopter[parent[l]] = 1
        leaf = next
        next = set([])
    return early_adopter.count(1)


N = int(sys.stdin.readline().rstrip())
graph = [-1 for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[max(u, v)] = min(u, v)
print(solve(graph, N))

if __name__ == "__main__":
    # test 1
    test = [-1, -1, 1, 1, 1, 2, 2, 4, 4]
    expected = 3
    result = solve(test, 8)
    if result != expected:
        print("test 1 fail, result:", result, ", expected:", expected)

    # test 2
    test = [-1, -1, 1, 1, 2, 3, 3, 4, 4, 4]
    expected = 3
    result = solve(test, 9)
    if result != expected:
        print("test 2 fail, result:", result, ", expected:", expected)

    # test 3
    test = [-1, -1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 8, 9, 9, 9, 9, 9]
    expected = 5
    result = solve(test, 16)
    if result != expected:
        print("test 3 fail, result:", result, ", expected:", expected)

    # test 4
    test = [-1, -1, 1, 2, 2, 4, 4, 6, 6, 8, 8]
    expected = 4
    result = solve(test, 10)
    if result != expected:
        print("test 4 fail, result:", result, ", expected:", expected)

    # test 5
    test = [-1, -1, 1, 2, 2, 4, 4]
    expected = 2
    result = solve(test, 6)
    if result != expected:
        print("test 5 fail, result:", result, ", expected:", expected)

    # test 6
    test = [-1, -1, 1, 2, 2, 2, 3, 6, 4, 4, 5, 1]
    expected = 5
    result = solve(test, 11)
    if result != expected:
        print("test 5 fail, result:", result, ", expected:", expected)
