import java.util.*;
class Solution {
    public int solution(String my_string) {
        
        int sum = Arrays.stream(my_string.replaceAll("[a-z]|[A-Z]", "").split(""))
            .mapToInt(Integer::parseInt)
            .sum();
        
        int answer = sum;
        return answer;
    }
}