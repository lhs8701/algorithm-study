N,M,L = list(map(int,input().split(' ')))

lst = [0]*N #공을 받은 횟수를 기억하기 위해 빈 배열을 만듭니다

#초기값을 적어줍니다
idx = 0 #첫번째 사람의 idx는 0입니다
lst[idx] = 1 #최초 1번이 공을 받습니다
cnt = 0 #cnt는 총 공을 던지는 횟수입니다
while True:
    
    if lst[idx] == M: #(idx+1)번째 사람이 M번의 공을 받았다면
        print(cnt) #정답을 출력한 뒤
        break #반복문을 멈춥니다

    if lst[idx]%2 == 0: #(idx+1)번째 사람이 짝수번째로 공을 받았으면
        idx = abs((idx-L) %N) # abs((idx-L)%N번째 사람에게 공을 줍니다 (시계 반대방향으로 공을 돌립니다)
        lst[idx] +=1 #공을 받은 사람의 횟수를 증가시킵니다
        cnt+=1 #전체 공이 움직인 횟수를 증가시킵니다
    else: #(idx+1)번째 사람이 홀수번째로 공을 받았으면
        idx=(idx+L)%N #시계방향으로 공을 돌립니다
        lst[idx] +=1
        cnt+=1