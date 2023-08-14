import sys
from collections import Counter


def backTracking(pre, l):
    answer = 0

    # 행운의 문자열이므로 1를 리턴
    if l == len(s):
        return 1

    # 반복문을 통해 단어를 확인
    for k in cnt.keys():
        # 현재 단어가 이전 단어일 경우와 현재 단어의 개수가 0일 경우 다음 단어를 확인한다.
        if k == pre or cnt[k] == 0:
            continue

        cnt[k] -= 1 # 현재 단어의 개수를 감소
        answer += backTracking(k, l + 1) # 백트래킹 후 리턴 받은 수를 answer에 더한다.
        cnt[k] += 1 # 현재 단어의 개수를 증가

    # answer 리턴
    return answer


s = list(map(str, sys.stdin.readline().strip()))
cnt = Counter(s) # 문자의 개수를 딕셔너리로 변환
print(backTracking('', 0))