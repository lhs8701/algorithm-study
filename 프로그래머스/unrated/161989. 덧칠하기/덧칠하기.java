import java.util.*;

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        boolean[] numbers = new boolean[n+1];
        Arrays.fill(numbers, true);
        for(int i : section){
            numbers[i] = false;
        }
        int cur = section[0];
        int cnt = 0;
        while(cur <= n){
            if (numbers[cur]){
                cur++;
            }
            else{
                cur+=m;
                cnt++;
            }
        }
        
        return cnt;
    }
}