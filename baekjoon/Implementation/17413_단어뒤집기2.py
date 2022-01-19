# import sys
#
# S = sys.stdin.readline().rstrip()
# flag = False
# temp = []
# for i in range(len(S)):
#     if flag:
#         print(S[i],end="")
#         if S[i] ==  '>':
#             flag = False
#         continue
#     if S[i] == ' ' or S[i] == '<':
#         temp.reverse()
#         print("".join(temp), end="")
#         temp = []
#         print(S[i],end="")
#         if S[i] == '<':
#             flag = True
#         continue
#     temp.append(S[i])
# temp.reverse()
# print("".join(temp),end="")

import sys

S = list(sys.stdin.readline().rstrip())
i = 0
start = 0
while i < len(S):
    if S[i] == '<':
        while S[i] != '>':
            i+=1
        i+=1
    elif S[i] == ' ':
        i += 1
    else:
        start = i
        while i < len(S) and S[i] != '<' and S[i]!= ' ':
            i+=1
        temp = S[start:i]
        temp.reverse()
        S[start:i] = temp

print("".join(S))
