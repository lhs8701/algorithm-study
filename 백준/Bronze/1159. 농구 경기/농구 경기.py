from sys import stdin
input = stdin.readline

n = int(input())
first = {chr(i):0 for i in range(97, 123)}

for i in range(n):
    first[input()[0]] += 1
answer = ""
for key, val in first.items():
    if val >= 5:
        answer += key

if answer:
    print(answer)
else:
    print("PREDAJA")