import java.util.*;

class Solution {
    public long solution(String numbers) {        
        Map<String, String> map = Map.of("zero", "0", "one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9");
        Set<String> keys = map.keySet();
        int start = 0;
        String answer = "";
        for(int end = 1; end <= numbers.length(); end++){
            String str = numbers.substring(start, end);
            if (keys.contains(str)){
                answer += map.get(str);
                start = end;
            }
        }
        return Long.parseLong(answer);
    }
}