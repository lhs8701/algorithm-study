def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
        
    

def solution(n):
    gc = gcd(6, n)
    lc = gc * 6//gc * n//gc
    return lc // 6
