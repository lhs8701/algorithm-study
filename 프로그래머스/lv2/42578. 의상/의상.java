import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Long> map = Arrays.stream(clothes)
            .collect(Collectors.groupingBy(arr -> arr[1], Collectors.counting()));
        long answer = 1L;
        for(Long num : map.values()){
            answer *= (num + 1);
        }
        return (int) answer - 1;
    }
}