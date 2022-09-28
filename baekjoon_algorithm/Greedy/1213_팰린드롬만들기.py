import sys

str = sys.stdin.readline().rstrip()
count = [0 for i in range(26)]
size_str = len(str)
middle = ""
ans = ""
flag = True
for i in range(size_str):
    count[ord(str[i]) - ord('A')] += 1

for i in range(26):
    if count[i] % 2 == 1:
        if middle == "":
            middle = chr(ord('A') + i)
        else:
            flag = False
            break
    ans += chr(ord('A') + i) * (count[i] // 2)

if flag:
    print(ans + middle + ans[::-1])
else:
    print("I'm Sorry Hansoo")
