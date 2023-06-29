import sys

word = str(sys.stdin.readline().rstrip("\n"))

# 반복문을 통해 문자를 확인
for i in range(len(word)):

    # i번째로 시작한 문자열과 i번째로 시작한 문자를 뒤에서부터 확인한 문자열을 확인
    # 같을 경우 i번째 이전에 문자가 다른 것으로 문자열 뒤에 추가해주면 된다.
    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break