import sys


def self_sum(n):
    r = n
    sum = 0
    while r:
        sum += r % 10
        r //= 10
    return sum + n


def self_number(numbers, n):
    r = n
    while True:
        r = self_sum(r)
        if r <= 10000:
            numbers[r] = 1
        else:
            break


numbers = [0] * 10001
for i in range(1, 10001):
    self_number(numbers, i)
for i in range(1, 10001):
    if numbers[i] == 0:
        print(i)
