import java.util.*;
class Solution {
    public Integer[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        while (n != 1){
            for(int i=2; i<=n; i++){
                if (n % i == 0) {
                    n /= i; 
                    if (!list.contains(i)){
                        list.add(i);    
                    }
                    break;
                }           
            }   
        }
    
        Integer[] answer = list.toArray(new Integer[list.size()]);
        return answer;
    }
}