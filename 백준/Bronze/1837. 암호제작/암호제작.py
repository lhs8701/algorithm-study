P, K = map(int, input().split())
bad_number = K # 더 작은 값을 출력할 때 비교할 변수로, 초깃값은 K를 주었다.

for i in range(2, K):
    if P % i == 0: # BAD 케이스에 해당되는 사례
        if bad_number > i:
            bad_number = i # p, q 중 더 작은 값을 알아내기 위함이다.

if bad_number != K: # 초깃값에서 변경되었다는 건 BAD케이스가 있다는 의미
    print('BAD', bad_number)
else:
    print('GOOD')