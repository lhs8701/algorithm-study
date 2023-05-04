class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<=n ;i++){
            boolean flag = false;
            for (int j=2; j<i; j++){
                if (i % j == 0){
                    flag = true;
                    break;
                }
            }
            if (flag){
                answer++;
            }
        }
        return answer;
    }
}