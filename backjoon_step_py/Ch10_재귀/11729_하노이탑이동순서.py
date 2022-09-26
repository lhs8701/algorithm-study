import sys

N = int(sys.stdin.readline().rstrip())


def func(num, h_from, h_to):
    global cnt
    if num == 0:
        return
    func(num - 1, h_from, 6 - (h_from + h_to))
    print(h_from, h_to)
    func(num - 1, 6 - (h_from + h_to), h_to)


ans = 1
for i in range(2, N + 1):
    ans = ans * 2 + 1
print(ans)
func(N, 1, 3)
