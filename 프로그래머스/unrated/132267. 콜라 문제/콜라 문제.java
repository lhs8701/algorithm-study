class Solution {
    public int solution(int a, int b, int n) {
        int x=n;
        int y=0;
        int answer=0;
        while(x / a != 0){
            y = x / a * b;
            x = x % a + y;
            answer+=y;
        }
        return answer;
    }
}