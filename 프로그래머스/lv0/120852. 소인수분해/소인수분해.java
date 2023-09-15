import java.util.*;
class Solution {
    public Integer[] solution(int n) {
        Set<Integer> set = new TreeSet<>();
        while (n != 1){
            for(int i=2; i<=n; i++){
                if (n % i == 0) {
                    n /= i; 
                    set.add(i);
                    break;
                }           
            }   
        }
    
        Integer[] answer = set.toArray(new Integer[set.size()]);
        return answer;
    }
}