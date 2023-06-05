import sys


def roundTraditional(val):
    return round(val + 10 ** (-len(str(val)) - 1))


n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
else:
    levels = []
    for _ in range(n):
        levels.append(int(sys.stdin.readline().rstrip()))
    levels.sort()
    sum_val = sum(levels)
    tip = roundTraditional(n * 15 / 100)
    print(roundTraditional(sum(levels[tip:n - tip]) / (n - 2 * tip)))
