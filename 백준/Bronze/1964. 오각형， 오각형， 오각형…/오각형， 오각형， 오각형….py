
n = int(input())

res = 5
plus_val = 7

for i in range(1, n):
    res += plus_val
    plus_val += 3
    
print(res % 45678)