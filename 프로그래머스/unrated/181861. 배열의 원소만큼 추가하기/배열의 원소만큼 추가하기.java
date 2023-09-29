import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        for(int num : arr){
            for(int i=0; i<num; i++){
                answer.add(num);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}