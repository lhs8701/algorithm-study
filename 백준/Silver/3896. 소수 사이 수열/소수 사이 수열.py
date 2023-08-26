T = int(input())
# 에라토스테네스의 체 구하기
sosu = [True] * (1299709 + 1)
sosu[0], sosu[1] = False, False
for i in range(1, 1299709 + 1):
    if not sosu[i]:
        continue
    for j in range(i * i, 1299709 + 1, i):
        sosu[j] = False

for _ in range(T):

    N = int(input())
    # 만약 소수 라면 0 출력
    if sosu[N]:
        print(0)
    else:  # 소수가 아니라면
        i = N  # 왼쪽으로 이동할 인덱스
        j = N  # 오른쪽으로 이동할 인덱스
        count = 1  # 개수를 저장할 인덱스(현재 개수 1개 저장)
        while True:  # 왼쪽이동 하면서 소수만나면 정지
            i -= 1
            if sosu[i]:
                break
            count += 1  # 지나면서 개수를 1개씩 추가해준다.
        while True:  # 오른쪽으로 이동하면서 소수 만나면 정지
            j += 1
            if sosu[j]:
                break
            count += 1  # 지나면서 개수를 1개씩 추가해준다.
        print(count + 1)