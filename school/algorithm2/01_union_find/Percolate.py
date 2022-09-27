import random
import sys
import math
import statistics


def root(ids, i):
    while i != ids[i]: i = ids[i]
    return i


def connected(ids, p, q):
    return root(ids, p) == root(ids, q)


def union(ids, size, p, q):
    id1, id2 = root(ids, p), root(ids, q)
    if id1 == id2: return
    if size[id1] <= size[id2]:
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]


def check_adjacent(ids, size, matrix, idx):
    if idx % n != 0 and matrix[idx - 1] == 1:
        union(ids, size, idx, idx - 1)
    if idx % n != n - 1 and matrix[idx + 1] == 1:
        union(ids, size, idx, idx + 1)
    if idx - n >= 0 and matrix[idx - n] == 1:
        union(ids, size, idx, idx - n)
    if idx + n < n * n and matrix[idx + n] == 1:
        union(ids, size, idx, idx + n)


def simulate(n, t):
    p_list = []
    for _ in range(t):
        matrix = [0 for _ in range(n * n)]
        ids, size = [], []

        for i in range(n * n + 2):
            ids.append(i)
            size.append(1)
        for i in range(n):
            union(ids, size, n * n, i)
            union(ids, size, n * n + 1, n * (n - 1) + i)

        cnt = 0
        while not connected(ids, n * n, n * n + 1):
            rand_num = 0
            while True:
                rand_num = random.randint(0, n * n - 1)
                if matrix[rand_num] == 0:
                    break
            matrix[rand_num] = 1
            cnt += 1
            check_adjacent(ids, size, matrix, rand_num)
        p = cnt / (n * n)
        p_list.append(p)

    mean_val = statistics.mean(p_list)
    stdev_val = statistics.stdev(p_list, xbar=None)
    confidence_start = mean_val - 1.96 * stdev_val / math.sqrt(t)
    confidence_end = mean_val + 1.96 * stdev_val / math.sqrt(t)

    print("mean = %.10f" % (mean_val))
    print("stdev = %.10f" % (stdev_val))
    print("95%% confidence interval = [%.10f, %.10f]" % (confidence_start, confidence_end))


n, t = map(int, sys.stdin.readline().rstrip().split())
simulate(n, t)
