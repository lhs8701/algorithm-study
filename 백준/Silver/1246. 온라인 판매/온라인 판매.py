import sys

n, m = map(int, sys.stdin.readline().split())
p = [int(sys.stdin.readline()) for _ in range(m)]
p.sort() # 오름차순 정렬
res = 0 # 수익
target = 0 # 책정한 가격
for i in range(m):
    egg = min(m - i, n) # 달걀보다 사는 사람이 많으면 예외 처리

    # 현재 수익보다 현재 달걀로 판매하는 수익이 더 클 경우
    if res < p[i] * egg:
        res = p[i] * egg # 수익 초기화
        target = p[i] # 달걀 책졍 가격 초기화

print(target, res)