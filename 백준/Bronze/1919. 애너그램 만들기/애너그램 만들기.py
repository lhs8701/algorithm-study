string = input()
target = input()

for s in string:
    if s in target:
        target=target.replace(s, '',1) # 뒤에 1은 치환횟수인데 1을 넣지 않으면 aab , a 일 때 b만 남게 됨
        string=string.replace(s, '',1)

sums = len(string)+len(target)
print(sums)