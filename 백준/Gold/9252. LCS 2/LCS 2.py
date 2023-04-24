import sys

str1 = list(str(sys.stdin.readline().rstrip()))
str2 = list(str(sys.stdin.readline().rstrip()))
len1 = len(str1)
len2 = len(str2)
dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = len2, len1
ans = []
while i != 0 and j != 0:
    if str2[i - 1] == str1[j - 1]:
        ans.append(str2[i - 1])
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
print(dp[len2][len1])
ans.reverse()
print("".join(ans))
