count = int(input())
a = 0
b = 0
num = list(map(int, input().split()))
for i in range(count):
    a += (num[i]//30+1)*10
    b += (num[i]//60+1)*15
if a > b:
    print('M', b)
elif a < b:
    print('Y', a)
else:
    print('Y', 'M', a)