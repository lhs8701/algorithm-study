import java.util.*;
import java.util.stream.*;
import java.util.stream.Collectors.*;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        Map<String, Long> xMap = Arrays.stream(X.split(""))
            .collect(Collectors.groupingBy(k -> k, Collectors.counting()));
        Map<String, Long> yMap = Arrays.stream(Y.split(""))
            .collect(Collectors.groupingBy(k -> k, Collectors.counting()));
        
        for(int i=9; i>=0; i--){
            String key = String.valueOf(i);
            long num = Math.min(xMap.getOrDefault(key, 0L), yMap.getOrDefault(key, 0L));
            answer += key.repeat((int)num);
        }
        return answer.isEmpty() ? "-1" : Arrays.stream(answer.split("")).allMatch(n -> n.equals("0")) ? "0" : answer;
    }
}