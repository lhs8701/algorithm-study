import java.util.List;

class Solution {
    public int solution(int hp) {
        List<Integer> arr = List.of(5, 3, 1);
        int cnt = 0;
        for (Integer i : arr){
            cnt += hp / i;
            hp%=i;
        }
        
        int answer = cnt;
        return answer;
    }
}