import math
import sys


#
# n = int(sys.stdin.readline().rstrip())
# first, second, answer = 0, 1, n
# for i in range(n - 1):
#     answer = first + second
#     first = second
#     second = answer
#
# print(answer)
#


def iterMeth(val, es, maxit):
    iter = 1
    sol = 0
    solold = 0
    ea = 100
    while True:
        if iter != 1:
            solold = sol
        sol += val ** (iter - 1) / math.factorial(iter - 1)
        iter += 1

        if sol != 0:
            ea = abs((sol - solold) / sol) * 100
        if ea <= es or iter >= maxit:
            break

    return sol


print(iterMeth(0.5, 0.05, 100))
