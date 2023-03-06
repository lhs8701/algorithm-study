import math
import sys


def init_palindrome_list():
    for i in range(START_IDX, END_IDX + 1):
        palindrome[i][i] = True

    for i in range(START_IDX, END_IDX):
        if str[i] == str[i + 1]:
            palindrome[i][i + 1] = True

    for k in range(2, END_IDX):
        for i in range(START_IDX, END_IDX + 1 - k):
            if str[i] == str[i + k] and palindrome[i + 1][i + k - 1]:
                palindrome[i][i + k] = True


def find_min_palindrome(end):
    min_val = math.inf
    for i in range(START_IDX, end + 1):
        if palindrome[i][end]:
            min_val = min(min_val, dp[i - 1])
    return min_val


str = sys.stdin.readline().rstrip()
str = '_' + str
palindrome = [[False for _ in range(len(str))] for _ in range(len(str))]
dp = [0 for _ in range(len(str))]
START_IDX = 1
END_IDX = len(str) - 1

init_palindrome_list()
for i in range(START_IDX, END_IDX + 1):
    dp[i] = min(dp[i - 1], find_min_palindrome(i)) + 1

print(dp[END_IDX])
